from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

import client_core.usuario.models


class CoreView(View):
    def get(self, *args, **kwargs):
        usuarios = ''
        if self.request.tenant.schema_name != 'public':
            usuarios = list(client_core.usuario.models.Usuario.objects.values('nome', 'idade'))
        response = {
            'status': True,
            'description': f'{self.request.tenant.name} Schema',
            'usuarios': usuarios if usuarios else "Schema principal não contem usuarios"
        }

        return JsonResponse(response, safe=False)