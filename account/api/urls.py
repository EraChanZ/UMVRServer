from account.api.views import registration_view, UserViewSet
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .router import UserRouter

app_name = "account"

urlpatterns = [
    path('register', registration_view, name='register'),
    path('login', obtain_auth_token, name='login'),
    path('', include(UserRouter.urls))
]