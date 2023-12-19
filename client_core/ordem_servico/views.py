from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.
class OrdemServicoView(APIView):
    def get(self, *args, **kwargs):
        response = {
            'status': True,
            'descricao': ''
        }

        return JsonResponse(response, safe=False)
