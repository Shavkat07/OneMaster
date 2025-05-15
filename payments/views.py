from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from fitness_clubs.permissions import IsTrainerOrAdmin
from payments.models import Payment
from payments.serializers import PaymentSerializer


# Create your views here.

class PaymentViewSet(ModelViewSet):
	queryset = Payment.objects.none()
	serializer_class = PaymentSerializer
	permission_classes = [IsAuthenticated, IsTrainerOrAdmin]

	def get_queryset(self):
		return Payment.objects.all()
