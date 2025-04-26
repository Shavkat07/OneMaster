from django.contrib import admin

from clients.models import Client, TrainingPlan


admin.site.register([Client, TrainingPlan])