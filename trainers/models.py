from django.contrib.auth.models import User
from django.db import models

from fitness_clubs.models import FitnessClub


# Create your models here.
class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # если используешь систему логинов
    full_name = models.CharField(max_length=255)
    fitness_club = models.ForeignKey(FitnessClub, on_delete=models.CASCADE)
    experience_years = models.IntegerField()
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='trainers/avatars/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
