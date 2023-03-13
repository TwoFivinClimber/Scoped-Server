from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .user import User



class Company(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.CharField(null=True, blank=True,max_length=100)
    logo = models.CharField(null=True, blank=True, max_length=100)
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=750)
    phone = PhoneNumberField(region='US', max_length=15)
    email = models.EmailField(max_length=100)
    location = models.CharField(max_length=50)
    lat = models.FloatField()
    long = models.FloatField()
    creation = models.DateField()
    
    
    