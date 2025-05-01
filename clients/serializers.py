from clients.models import Client, TrainingPlan
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class TrainingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingPlan
        fields = '__all__'


