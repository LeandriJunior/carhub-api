from django.db import models

import core.models


# Create your models here.

class PontoFuncao(core.models.Log):
    nome = models.CharField(max_length=255, primary_key=True)
    nm_descritivo = models.CharField(max_length=512, null=True)
    descricao = models.CharField(max_length=1024, null=True)
    modulo = models.CharField(max_length=64, null=True)
    ponto_funcao_pai = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True)
    prioridade = models.IntegerField(null=True)

    class Meta:
        db_table = 'sistema_pontofuncao'


class Grupo(core.models.Log):
    nome = models.CharField(max_length=255, primary_key=True)
    nm_descritivo = models.CharField(max_length=512, null=True)
    descricao = models.CharField(max_length=1024, null=True)
    modulo = models.CharField(max_length=64, null=True)
    grupo_pai = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True)
    prioridade = models.IntegerField(null=True)
    class Meta:
        db_table = 'sistema_grupo'


class GrupoPontoFuncao(core.models.Log):
    grupo = models.ForeignKey('Grupo', on_delete=models.DO_NOTHING, null=True )
    ponto_funcao = models.ForeignKey('PontoFuncao', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = 'sistema_grupo_pontofuncao'

