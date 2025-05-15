from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from fitness_clubs.models import FitnessClub
from fitness_clubs.permissions import IsTrainerOrAdmin
from fitness_clubs.serializers import FitnessClubSerializer


# Create your views here.
class FitnessClubsViewSet(ModelViewSet):
	queryset = FitnessClub.objects.none()
	serializer_class = FitnessClubSerializer
	permission_classes = [IsAuthenticated, IsTrainerOrAdmin]

	def get_queryset(self):
		return FitnessClub.objects.all()

