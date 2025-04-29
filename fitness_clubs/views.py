from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from fitness_clubs.models import FitnessClub
from fitness_clubs.serializers import FitnessClubSerializer


# Create your views here.
class FitnessClubsViewSet(ModelViewSet):
	queryset = FitnessClub.objects.none()
	serializer_class = FitnessClubSerializer

	def get_queryset(self):
		return FitnessClub.objects.all()

