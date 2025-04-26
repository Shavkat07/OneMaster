from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TrainersViewSet

router = DefaultRouter()

router.register(r'trainers', TrainersViewSet, basename='trainers')

urlpatterns = [
	path('', include(router.urls)),  # Все `ViewSet` уже включены сюда
]



