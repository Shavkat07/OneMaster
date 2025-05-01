from django.db import models
from trainers.models import Trainer
# Create your models here.

class Client(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10)
    goals = models.TextField(blank=True)  # похудеть, набрать массу и т.п.
    health_notes = models.TextField(blank=True)  # противопоказания
    created_at = models.DateTimeField(auto_now_add=True)



class TrainingPlan(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()  # например: кардио + силовые
    completed = models.BooleanField(default=False)

