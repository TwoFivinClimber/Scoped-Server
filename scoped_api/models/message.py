from django.db import models
from .user import User
from .job import Job

class Message(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='messages')
    content = models.CharField(max_length=200)
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
