from django.db import models

from clients.models import Client


# Create your models here.
class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateField()
    comment = models.TextField(blank=True)
    is_confirmed = models.BooleanField(default=True)
