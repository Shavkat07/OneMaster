from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from clients.serializers import ClientSerializer, TrainingPlanSerializer
from clients.models import Client


# Create your views here.

class ClientViewSet(ModelViewSet):
	queryset = Client.objects.none()
	serializer_class = ClientSerializer

	def get_queryset(self):
		return Client.objects.all()



class TrainingPlanViewSet(ModelViewSet):
	queryset = Client.objects.all()
	serializer_class = TrainingPlanSerializer

