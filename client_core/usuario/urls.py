from django.urls import path, include
import client_core.login.urls
urlpatterns = [
    path('', include(client_core.login.urls))
]