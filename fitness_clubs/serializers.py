from rest_framework import serializers

from fitness_clubs.models import FitnessClub


class FitnessClubSerializer(serializers.ModelSerializer):
	class Meta:
		model = FitnessClub
		fields = '__all__'

