from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView

import BO.sqlalchemy.integracao


# Create your views here.

class Teste(APIView):
    def get(self, *args, **kwargs):
        sql = BO.sqlalchemy.integracao.SqlAlchemy(schema=self.request.tenant.schema_name)

        response = {'usuarios': sql.select(tabela='usuario')}

        return JsonResponse(response, safe=False)