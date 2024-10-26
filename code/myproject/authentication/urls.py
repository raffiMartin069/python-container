from django.urls import path
from authentication.views import LoginView
from myproject.api_version import API_VERSION


urlpatterns = [
    path(f'{API_VERSION}/auth/', LoginView.as_view()),
]