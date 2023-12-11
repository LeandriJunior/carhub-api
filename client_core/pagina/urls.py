from django.urls import re_path
from client_core.pagina import views as pagina
urlpatterns = [
    re_path('buscar_pagina', pagina.GetPaginaView().as_view()),
]