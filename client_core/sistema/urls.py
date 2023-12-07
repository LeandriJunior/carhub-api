from django.urls import re_path

import client_core.sistema.views

urlpatterns = [
    re_path('teste/', client_core.sistema.views.Teste.as_view())
]