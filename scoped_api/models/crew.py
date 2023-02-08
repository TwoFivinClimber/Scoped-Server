from django.db import models
from .user import User
from .job import Job
from .skill import Skill

class Crew(models.Model):
    uid= models.ForeignKey(User, on_delete=models.CASCADE)
    job= models.ForeignKey(Job, on_delete=models.CASCADE)
    skill= models.ForeignKey(Skill, null=True, on_delete=models.DO_NOTHING)
    accepted= models.BooleanField(null=True, blank=True)
