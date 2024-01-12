from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

from BO.client_core.ordem_servico.ordem_servico import OrdemServico


# Create your views here.
class OrdemServicoView(APIView):
    def get(self, *args, **kwargs):
        status, descricao, data = OrdemServico().get_ordem_servico()

        response = {
            'status': True,
            'descricao': '',
            'dados': data
        }
        return JsonResponse(response, safe=False)
