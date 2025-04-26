from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PaymentViewSet

router = DefaultRouter()

router.register(r'trainers', PaymentViewSet, basename='trainers')

urlpatterns = [
	path('', include(router.urls)),  # Все `ViewSet` уже включены сюда
]
