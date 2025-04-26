from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from trainers.models import Trainer
from trainers.serializers import TrainerSerializer


# Create your views here.
class TrainersViewSet(ModelViewSet):
	model = Trainer
	serializer_class = TrainerSerializer
