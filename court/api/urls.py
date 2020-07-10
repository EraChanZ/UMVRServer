from .router import CourtRouter
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

app_name = "court"

urlpatterns = [
    path('', include(CourtRouter.urls))
]