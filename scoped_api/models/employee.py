from django.db import models
from .company import Company
from .user import User


class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='employees')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='companies')
    admin = models.BooleanField(default=False)
    creation = models.DateField()
    
    @property
    def skills(self):
        return self.__skills
    
    @skills.setter
    def skills(self, value):
        self.__skills = value
