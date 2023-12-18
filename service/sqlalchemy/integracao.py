from __future__ import annotations

from typing import Optional

import psycopg2
import sqlalchemy as sql
from sqlalchemy import text, Table
from sqlalchemy.orm import sessionmaker, scoped_session

from cartech.settings import DATABASES


class SqlAlchemy:
    def __init__(self,
                 user=DATABASES['default']['USER'], password=DATABASES['default']['PASSWORD'],
                 host=DATABASES['default']['HOST'], port=DATABASES['default']['PORT'],
                 database=DATABASES['default']['NAME'], schema=None
                 ):

        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.schema = schema
        self.engine = None
        self.conexao = None
        self.metadata = None
        self.session = None
        self.resultset = None
        self.scoped_session = None
        self.conectar()

    def conectar(self):
        database_url = 'postgresql+psycopg2://{user}:{password}@{host}/{database_name}'.format(
            user=self.user,
            password=self.password,
            host=self.host,
            database_name=self.database,
        )

        self.engine = sql.create_engine(database_url)
        self.conexao = self.engine.connect()
        self.metadata = sql.MetaData(schema=self.schema)
        self.scoped_session = scoped_session(sessionmaker(bind=self.engine))

    def cria_sessao(self):
        self.session = self.scoped_session()

    def remove_sessao(self):
        self.scoped_session.remove()

    def get_conexao(self):
        return self.conexao

    def criar_tabela_meta(self, nm_tabela):
        table = sql.Table(nm_tabela, self.metadata, autoload=True, autoload_with=self.engine)

        return table

    def buscar(self, query=None, retorno_dict=True):
        with self.conexao.begin():
            self.resultset = self.conexao.execute(text(query))

        return self.resultset if not retorno_dict else self.get_dict()

    def buscar_sessao(self, query=None, params=None, retorno_dict=True):
        try:
            self.cria_sessao()
            with self.session.begin():
                self.resultset = self.session.execute(text(query), params)
            self.remove_sessao()
            return True, '', self.resultset if not retorno_dict else self.get_dict()
        except:
            self.remove_sessao()
            return False, 'Erro ao buscar sessão', None

    def get_dict(self, valor_vazio=None):
        if not self.resultset:
            return False
        return [row._asdict() for row in self.resultset]
        d, resultlist = {}, []
        for i in self.resultset:
            for column, value in i._mapping.items():
                d = {**d, **{column: value}}
                if valor_vazio is not None:
                    d = {k: valor_vazio if not v else v for k, v in d.items()}
            resultlist.append(d)

        return resultlist

    def buscar_tabela(self, tabela=None, lista_colunas=None, filtro_where=None):
        try:
            colunas = ','.join(lista_colunas) if lista_colunas else '*'
            query = f'select {colunas} from {tabela} '

            if filtro_where:
                query += f'where '

                for chave, valor in filtro_where.items():
                    if type(valor) == list:
                        lista_valores = ','.join(valor)
                        query += f' {chave} in ({lista_valores}) and'

                    else:
                        query += f' {chave} = {valor} and'

                query = query[:-3] + ';'  # Removendo o ultimo 'and' e adcionando o ; no final

            self.cria_sessao()
            with self.session.begin():
                self.resultset = self.session.execute(text(query))
            self.remove_sessao()

            return True, '', self.get_dict()
        except:
            self.remove_sessao()
            return False, 'Erro ao buscar dados', []

    def inserir(self, nm_tabela=None, lista_colunas=None, lista_valores=None, nm_pk=None):
        try:
            colunas = ','.join(lista_colunas)
            valores = ','.join(lista_valores)
            nm_pk = nm_pk or self.get_tabela_pk(nm_tabela=nm_tabela)
            query = f'insert into {nm_tabela}({colunas}) values ({valores}) RETURNING {nm_pk};'

            self.cria_sessao()
            with self.session.begin():
                self.resultset = self.session.execute(text(query))
            self.remove_sessao()

            return True, '', self.resultset
        except:
            self.remove_sessao()
            return False, 'Erro ao inserir na tabela', None

    def update(self, nm_tabela=None, lista_colunas=None, lista_valores=None, filtro_where=None, nm_pk=None):
        try:
            nm_pk = nm_pk or self.get_tabela_pk(nm_tabela=nm_tabela)

            query = f'update {nm_tabela} set'

            for contador in range(len(lista_colunas)):
                query += f' {lista_colunas[contador]} = {lista_valores[contador]},'
            query = query[:-1]
            if filtro_where:
                query += f' where '

                for chave, valor in filtro_where.items():
                    if type(valor) == list:
                        lista_valores = ','.join(valor)
                        query += f' {chave} in ({lista_valores}) and'

                    else:
                        query += f' {chave} = {valor} and'

                query = query[:-3]  # Removendo o ultimo 'and'

            query += f" Returning {nm_pk};"

            self.cria_sessao()
            with self.session.begin():
                self.resultset = self.session.execute(text(query))
            self.remove_sessao()

            return True, '', self.resultset
        except:
            self.remove_sessao()
            return False, 'Erro ao atualizar tabela', None

    def get_tabela_pk(self, nm_tabela=None, schema=None):
        try:
            table = Table(nm_tabela, self.metadata, autoload=True, autoload_with=self.engine, schema=schema)

            primaryKeyColName = table.primary_key.columns.values()[0].name
            return True, '', primaryKeyColName
        except:
            return False, 'Erro ao buscar PK', None

    def select(self, coluna='*', tabela=None, filtro=None, dict=True):
        with self.conexao.begin():
            query = f"select {coluna} from {self.schema}.{tabela}"

            if filtro:
                query += f'where {filtro}'

            self.resultset = self.conexao.execute(text(query))

        return self.resultset if not dict else self.get_dict()


