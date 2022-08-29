from django.db import models
from super_types.models import SuperType

# Create your models here.

class Supers(models.Model):
    name = models.CharField(max_length=75)
    alter_ego = models.CharField(max_length=75)
    primary_ability = models.CharField(max_length=100)
    secondary_ability = models.CharField(max_length=100)
    catchphrase = models.CharField(max_length=200)
    super_type = models.ForeignKey(SuperType, on_delete=models.CASCADE)


