from django.db import models

class Gear(models.Model):
    name= models.CharField(max_length=50)
