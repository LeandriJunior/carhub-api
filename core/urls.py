from django.urls import re_path
import core.views

urlpatterns = [
    re_path('', core.views.CoreView.as_view(), name='core')
]