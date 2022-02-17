from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from core.views import (
    LoginView, LogoutView
)

urlpatterns = [
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('gettoken', obtain_auth_token, name='gettoken'),
]
