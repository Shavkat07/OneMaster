from django.db import models

from clients.models import Client


# Create your models here.
class Visit(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()
    attended = models.BooleanField(default=False)
