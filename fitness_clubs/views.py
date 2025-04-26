from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from fitness_clubs.models import FitnessClub
from fitness_clubs.serializers import FitnessClubSerializer


# Create your views here.
class FitnessClubsViewSet(ModelViewSet):
	model = FitnessClub
	serializer_class = FitnessClubSerializer
