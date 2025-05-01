from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from trainers.models import Trainer


class TrainerSerializer(ModelSerializer):
	user = UserDetailsSerializer(read_only=True)
	avatar = serializers.ImageField(max_length=None, required=False)

	class Meta:
		model = Trainer
		fields = '__all__'
