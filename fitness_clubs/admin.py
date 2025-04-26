from django.contrib import admin
from .models import FitnessClub


# Register your models here.
admin.site.site_header = "Fitness Clubs Administration"
admin.site.register(FitnessClub)




