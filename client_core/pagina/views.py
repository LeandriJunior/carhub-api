from django.http import JsonResponse
from rest_framework.views import APIView

import service.client_core.sistema.pagina.pagina as BOPagina


# Create your views here.


class GetPaginaView(APIView):
    def get(self, *args, **kwargs):
        pagina = self.request.GET.get('pagina')

        response = BOPagina.Pagina.get_pagina(pagina=pagina)

        return JsonResponse(response, safe=True)
