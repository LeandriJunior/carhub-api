from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt

from client_core.login import views as login
from client_core.usuario import urls as usuario
from client_core.sistema import urls as sistema

urlpatterns = [
    path('api/registrar', csrf_exempt(login.RegisterUserView().as_view())),
    path('api/login', csrf_exempt(login.LoginUserView().as_view())),
    path('api/home', csrf_exempt(login.HomeTestView().as_view())),
    re_path('api/usuario', include(usuario)),
    re_path('api/sistema', include(sistema)),
]
