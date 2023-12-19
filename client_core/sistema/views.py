from django.http import JsonResponse
from rest_framework.views import APIView

import service.sqlalchemy.integracao


# Create your views here.

class Teste(APIView):
    def get(self, *args, **kwargs):
        sql = service.sqlalchemy.integracao.SqlAlchemy(schema=self.request.tenant.schema_name)

        response = {'usuarios': sql.select(tabela='usuario')}

        return JsonResponse(response, safe=False)