from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from clients.serializers import ClientSerializer
from clients.models import Client


# Create your views here.

class ClientViewSet(ModelViewSet):
	model = Client
	serializer_class = ClientSerializer