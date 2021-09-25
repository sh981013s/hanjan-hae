from os import name
from django.db import models

# Create your models here.
class Alcohol(models.Model):
    name = models.CharField(max_length=100)
    alc = models.FloatField(max_length=3)
    cup = models.FloatField(max_length=6)
    bottle = models.FloatField(max_length=6)
    alc_type = models.CharField(max_length=50)
    company = models.CharField(max_length=50)

    def __str__ (self):
        return self.name
