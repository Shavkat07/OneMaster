from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FitnessClubsViewSet

router = DefaultRouter()

router.register(r'fitnessclubs', FitnessClubsViewSet, basename='trainers')

urlpatterns = [
	path('', include(router.urls)),  # Все `ViewSet` уже включены сюда
]
