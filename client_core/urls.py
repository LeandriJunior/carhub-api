from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

import client_core.usuario.urls
import client_core.login.urls
from client_core.login.views import RegisterUserView, LoginUserView

urlpatterns = [
    path('registrar', csrf_exempt(RegisterUserView.as_view())),
    path('login', csrf_exempt(LoginUserView.as_view())),

    path('usuario', include(client_core.usuario.urls)),
]