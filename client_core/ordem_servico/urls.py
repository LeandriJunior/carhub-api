from django.urls import re_path

from client_core.ordem_servico import views
urlpatterns = [
    re_path('lista', views.OrdemServicoView.as_view())
]
