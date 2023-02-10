from django.db import models
from .user import User
from .skill import Skill

class UserSkill(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name='skills')
    skill= models.ForeignKey(Skill, on_delete=models.CASCADE)
