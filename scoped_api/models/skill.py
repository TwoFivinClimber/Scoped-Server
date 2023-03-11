from django.db import models
from .company import Company

class Skill(models.Model):
    skill= models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    