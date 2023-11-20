from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

import client_core.usuario.urls
import client_core.login.urls
import client_core.login.views

urlpatterns = [
    path('registrar', csrf_exempt(client_core.login.views.RegisterUserView().as_view())),
    path('login', csrf_exempt(client_core.login.views.LoginUserView().as_view())),

    path('usuario', include(client_core.usuario.urls)),
]
