from django.db import models
from .company import Company
from .employee import User

class Blog(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=2000)
    datetime = models.DateTimeField()
    
