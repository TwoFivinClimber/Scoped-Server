from django.db import models
from .company import Company
from .employee import Employee

class Blog(models.Model):
    uid = models.ForeignKey(Employee, on_delete=models.DO_NOTHING)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    datetime = models.DateTimeField()
    
