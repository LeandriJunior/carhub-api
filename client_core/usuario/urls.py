from django.urls import path
import client_core.usuario.views

urlpatterns = [
    path('', client_core.usuario.views.UsuarioView.as_view())
]