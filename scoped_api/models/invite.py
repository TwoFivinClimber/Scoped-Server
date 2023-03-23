from django.db import models
from .user import User
from .company import Company

class Invite(models.Model):
    uid= models.ForeignKey(User, on_delete=models.CASCADE, related_name='invites')
    company= models.ForeignKey(Company, on_delete=models.CASCADE, related_name='invites')
    