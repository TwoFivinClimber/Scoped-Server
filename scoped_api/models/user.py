from django.db import models


class User(models.Model):
    firebase= models.CharField(max_length=50)
    name= models.CharField(max_length= 100)
    bio= models.CharField(max_length=500)
    image= models.CharField(max_length=100)
    
    