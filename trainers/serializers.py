from rest_framework.serializers import ModelSerializer

from trainers.models import Trainer


class TrainerSerializer(ModelSerializer):
	class Meta:
		model = Trainer
		fields = '__all__'
