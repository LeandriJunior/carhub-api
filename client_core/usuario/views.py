from django.http import JsonResponse
from django.shortcuts import render
from django.views import View


class UsuarioView(View):
    def get(self, *args, **kwargs):
        response = {
            'status': True,
            'description': 'Public Schema'
        }

        return JsonResponse(response, safe=False)