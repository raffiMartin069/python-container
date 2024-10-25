from django.urls import path
from myproject.api_version import API_VERSION
from django.views.generic import TemplateView

urlpatterns = [
    path(f'{API_VERSION}/auth/', TemplateView.as_view(template_name = 'login.html')),
]