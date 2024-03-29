from django.db import models
from .user import User
from .skill import Skill
from .company import Company

class Job(models.Model):
    uid= models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')
    company= models.ForeignKey(Company, on_delete=models.CASCADE)
    title= models.CharField(max_length=50)
    description= models.CharField(max_length=2000)
    datetime= models.DateTimeField()
    location= models.CharField(max_length=100)
    address= models.CharField(max_length=50)
    lat= models.FloatField()
    long= models.FloatField()
    category= models.ForeignKey(Skill, null=True, on_delete=models.SET_NULL)
    
    @property
    def messages(self):
        """returns messages for job"""
        job_messages = [m for m in self.job_messages.all()]
        return job_messages
    
    @property
    def gear(self):
        return self.__gear
    
    @gear.setter
    def gear(self, value):
        self.__gear = value
    
    @property
    def crew(self):
        return self.__crew
    
    @crew.setter
    def crew(self, value):
        self.__crew = value
        
    @property
    def accepted(self):
        return self.__accepted
    
    @accepted.setter
    def accepted(self, value):
        self.__accepted = value
        
    @property
    def images(self):
        return self.__images
        
    @images.setter
    def images(self, value):
        self.__images = value
