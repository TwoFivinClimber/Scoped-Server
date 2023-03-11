from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=750)
    location = models.CharField(max_length=50)
    lat = models.FloatField()
    long = models.FloatField()
    creation = models.DateField()
    
    
    