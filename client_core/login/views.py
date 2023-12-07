import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
import client_core.usuario.models
import BO.client_core.login.login


# Create your views here.

class LoginUserView(APIView):
    def get(self, *args, **kwargs):
        login = BO.client_core.login.login.Login.get_config_login()

        return JsonResponse(login, safe=False)
    def post(self, request):
        data = json.loads(self.request.body)

        sistema = BO.client_core.login.login.Login(
                                            request=self.request,
                                            username=data.get('username'),
                                            password=data.get('password')
                                            )

        status, descricao, response = sistema.login()

        response = {
            'status': status,
            'description': descricao,
            'response': response
        }
        return JsonResponse(response)


class RegisterUserView(APIView):
    # Classe temporaria, apenas para registrar pessoas momentaniamente
    def post(self, request):
        try:
            response = json.loads(self.request.body)
            username = f"{response['nm_primeiro']}.{response['nm_ultimo']}"
            client_core.usuario.models.UsuarioLogin.objects.create_user(username=username,
                                                                                  email=response['email'],
                                                                                  password=response['password'],
                                                                                  nm_primeiro=response['nm_primeiro'],
                                                                                  nm_ultimo=response['nm_ultimo'])

            status = {'status': True}
        except Exception as e:
            status = {'status': False,
                      'description': e}
        return JsonResponse(status)
