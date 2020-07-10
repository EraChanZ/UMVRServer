from .views import UserViewSet
from rest_framework import routers

UserRouter = routers.DefaultRouter()
UserRouter.register('user', UserViewSet)