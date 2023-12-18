from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt

from client_core.login import urls as login
from client_core.usuario import urls as usuario
from client_core.sistema import urls as sistema
from client_core.pagina import urls as pagina

urlpatterns = [
    re_path('api/', include(login)),
    re_path('api/usuario', include(usuario)),
    re_path('api/pagina', include(pagina)),
    re_path('api/sistema', include(sistema)),
]
