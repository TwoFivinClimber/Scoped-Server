from django.db import models
from .job import Job

class Image(models.Model):
    job= models.ForeignKey(Job, on_delete=models.CASCADE)
    image= models.CharField(max_length=100)
    description= models.CharField(max_length=500, null=True, default=None)
