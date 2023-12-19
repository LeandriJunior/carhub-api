from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt
from client_core.login.views import RegisterUserView, LoginUserView

urlpatterns = [
    re_path('registrar', csrf_exempt(RegisterUserView().as_view())),
    re_path('login', csrf_exempt(LoginUserView().as_view())),
]