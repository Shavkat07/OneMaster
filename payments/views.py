from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from payments.models import Payment
from payments.serializers import PaymentSerializer


# Create your views here.

class PaymentViewSet(ModelViewSet):
	queryset = Payment.objects.none()
	serializer_class = PaymentSerializer

	def get_queryset(self):
		return Payment.objects.all()
