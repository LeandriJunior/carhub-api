from typing import Optional

import jwt
from django.contrib.auth import authenticate, user_logged_in
from rest_framework_jwt.utils import jwt_payload_handler

import BO.client_core.login.section
from cartech import settings


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
                status, descricao, sessao = BO.client_core.login.section.Section(user=user).access_section()

                response = {
                    'user_name': user['user'].nm_primeiro+ ' ' + user['user'].nm_ultimo,
                    'user_token': user.get('token')
                }
                return status, descricao, response
            return False, 'Username ou senha Incorretos', None
        except TypeError:
            return False, 'Erro ao efetuar login', None

    def authenticate(self):
        try:
            self.user = authenticate(username=self.username, password=self.password)

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
