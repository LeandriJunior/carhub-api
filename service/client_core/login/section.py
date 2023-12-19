from django.db.models import F

import client_core.sistema.permissao.models


class Section:

    def __init__(self, user=None):
        self.user = user['user']
        self.nome = None
        self.ponto_funcao = None
        self.grupos = None
        self.tela_principal = None
        self.schema = None
        self.logo_empresa = None

    def section(self):
        response = {
            'nm_primeiro': self.user.nm_primeiro,
            'nm_completo': self.user.nm_primeiro + ' ' + self.user.nm_ultimo,
            'ponto_funcao': self.ponto_funcao,
            'grupos': self.grupos,
            'tela_principal': self.tela_principal,
            'schema': self.schema,
            'logo_empresa': self.logo_empresa
        }

        return True, '', response

    def fazer(self):

        self.__grupos_usuario()
        self.__ponto_funcao_usuario()
        self.__tela_principal_usuario()
        self.__schema_usuario()
        self.__schema_usuario()
        self.__logo_empresa()
        return self.section()
    def __grupos_usuario(self):
        self.grupos = list(client_core.sistema.permissao.models.GrupoUser.objects.filter(
            status=True, grupo__status=True, user_id=self.user.pk
        ).values_list('grupo_id', flat=True))


    def __ponto_funcao_usuario(self):
        pass

    def __tela_principal_usuario(self):
        tela = client_core.sistema.permissao.models.GrupoUser.objects.filter(
            status=True, user_id=self.user.pk
        ).values(tela_principal=F('grupo_id__tela_principal')).first()

        self.tela_principal = tela.get('tela_principal')
    def __schema_usuario(self):
        pass

    def __logo_empresa(self):
        logo_empresa = client_core.pagina.models.Pagina.objects.filter(status=True, nome='login').values(
            logo=F('configuracao__logo')
        ).first()

        self.logo_empresa = logo_empresa.get('logo')



