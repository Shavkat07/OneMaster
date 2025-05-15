from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from trainers.models import Trainer
from trainers.serializers import TrainerSerializer


# Create your views here.
class TrainersViewSet(ModelViewSet):
	queryset = Trainer.objects.all()
	serializer_class = TrainerSerializer
	permission_classes = [IsAuthenticated, IsAdminUser]
