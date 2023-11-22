

class Section:

    def __init__(self, user=None):
        self.user = user
        self.nome = None
        self.ponto_funcao = None
        self.grupos = None
        self.tela_principal = None
        self.schema = None

    def access_section(self):

        response = {
            'nome': self.user.,
            'ponto_funcao': self.ponto_funcao,
            'grupos': self.grupos,
            'tela_principal': self.tela_principal,
            'schema': self.schema
        }

        return True, '', response
