from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .user import User



class Company(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    logo = models.CharField(null=True, blank=True, max_length=100)
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=750)
    phone = PhoneNumberField(region='US', max_length=15)
    email = models.EmailField(max_length=100)
    location = models.CharField(null=True, blank=True, max_length=50)
    lat = models.FloatField(null=True, blank=True,)
    long = models.FloatField(null=True, blank=True,)
    creation = models.DateField()
    
    
    @property
    def admin(self):
        return self.__admin
    
    @admin.setter
    def admin(self, value):
        self.__admin = value
        
    @property
    def isowner(self):
        return self.__isowner
    
    @isowner.setter
    def isowner(self, value):
        self.__isowner = value
        
    @property
    def invited(self):
        return self.__invited
    
    @invited.setter
    def invited(self, value):
        self.__invited = value
