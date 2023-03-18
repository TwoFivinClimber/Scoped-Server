from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class User(models.Model):
    firebase= models.CharField(max_length=50)
    name= models.CharField(max_length= 100)
    phone = PhoneNumberField(region='US', max_length=15)
    email = models.EmailField(max_length=100)
    bio= models.CharField(max_length=500)
    image= models.CharField(max_length=100)
    
    
    @property
    def compskills(self):
        return self.__compskills
    
    @compskills.setter
    def compskills(self, value):
        self.__compskills = value
   
      