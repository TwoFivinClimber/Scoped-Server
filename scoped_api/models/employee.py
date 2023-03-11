from django.db import models
from .company import Company
from .user import User


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    admin = models.BooleanField(default=False)
    creation = models.DateField()
