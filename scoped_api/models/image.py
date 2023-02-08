from django.db import models
from django.core.validators import FileExtensionValidator
from .job import Job

class Image(models.Model):
    job= models.ForeignKey(Job, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='job_images/',
                             validators=[FileExtensionValidator(['jpg', 'jpeg', 'png', 'heic'])])
    description= models.CharField(max_length=500, null=True, default=None)
