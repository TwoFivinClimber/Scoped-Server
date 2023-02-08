from django.db import models
from .gear import Gear
from .job import Job


class JobGear(models.Model):
    job= models.ForeignKey(Job, on_delete=models.CASCADE)
    gear= models.ForeignKey(Gear, on_delete=models.CASCADE)
