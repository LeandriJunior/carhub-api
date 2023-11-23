import client_core.sistema.permissao.models


class Section:

    def __init__(self, user=None):
        self.user = user['user']
        self.nome = None
        self.ponto_funcao = None
        self.grupos = None
        self.tela_principal = None
        self.schema = None

    def section(self):
        response = {
            'nm_primeiro': self.user.nm_primeiro,
            'nm_completo': self.user.nm_primeiro + ' ' + self.user.nm_ultimo,
            'ponto_funcao': self.ponto_funcao,
            'grupos': self.grupos,
            'tela_principal': self.tela_principal,
            'schema': self.schema
        }

        return True, '', response

    def fazer(self):
        self.grupos_usuario()
        self.ponto_funcao_usuario()
        self.tela_principal_usuario()
        self.schema_usuario()
        return self.section()
    def grupos_usuario(self):
        self.grupos = list(client_core.sistema.permissao.models.GrupoUser.objects.filter(
            status=True, grupo__status=True, user_id=self.user.pk
        ).values_list('grupo_id', flat=True))


    def ponto_funcao_usuario(self):
        pass

    def tela_principal_usuario(self):
        pass

    def schema_usuario(self):
        pass



