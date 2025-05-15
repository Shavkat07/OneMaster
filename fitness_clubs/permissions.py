from rest_framework.permissions import BasePermission
from trainers.models import Trainer


class IsTrainerOrAdmin(BasePermission):
	"""
	    Проверяет, что пользователь — админ или связан с моделью Trainer.
	"""

	def has_permission(self, request, view):
		user = request.user
		if not user.is_authenticated:
			return False

		return user.is_staff or Trainer.objects.filter(user=user).exists()


