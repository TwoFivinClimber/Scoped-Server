from django.db import models
from .user import User
from .skill import Skill

class Job(models.Model):
    uid= models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=50)
    description= models.CharField(max_length=2000)
    datetime= models.DateTimeField()
    location= models.CharField(max_length=100)
    address= models.CharField(max_length=50)
    lat= models.FloatField()
    long= models.FloatField()
    category= models.ForeignKey(Skill, null=True, on_delete=models.SET_NULL)
    
