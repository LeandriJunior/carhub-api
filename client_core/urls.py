from django.urls import path, include
import client_core.usuario.urls
urlpatterns = [
    path('', include(client_core.usuario.urls))
]