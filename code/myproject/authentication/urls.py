from django.urls import path
from myproject.api_version import API_VERSION

from . import views

urlpatterns = [
    path(f'{API_VERSION}/auth', views.index, name="index"),
]