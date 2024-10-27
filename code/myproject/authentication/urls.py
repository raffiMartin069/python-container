from django.urls import path
from authentication.views import LoginView, SignUpView
from myproject.api_version import API_VERSION


urlpatterns = [
    path('', LoginView.as_view()),
    path(f'auth/', LoginView.as_view()),
    path('signup/', SignUpView.as_view()),
]