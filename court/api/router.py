from .views import CourtViewSet
from rest_framework import routers

CourtRouter = routers.DefaultRouter()
CourtRouter.register('court', CourtViewSet)
