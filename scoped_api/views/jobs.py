# from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scoped_api.models import Job, Skill, User, JobGear, Gear

class JobView(ViewSet):
  
    def list(self, request):
      
        jobs = Job.objects.all()
        
        jobs_serialized = JobSerializer(jobs, many=True)
        
        return Response(jobs_serialized.data)
    
    def retrieve(self, request, pk):

        job = Job.objects.get(pk=pk)
        
        job_serialized = JobSerializer(job)
        
        return Response(job_serialized.data)
    
    def create(self, request):
      
        cat = Skill.objects.get(pk=request.data['category'])
        user = User.objects.get(pk=request.data['uid'])

        job = Job.objects.create(
          title = request.data['title'],
          description = request.data['description'],
          datetime = request.data['datetime'],
          location = request.data['location'],
          address = request.data['address'],
          lat = request.data['lat'],
          long = request.data['long'],
          category = cat,
          uid = user
        )
        
        job_gear = request.data['gear']
        
        for item in job_gear:
            JobGear.objects.create(gear = Gear.objects.get(pk=item), job = job)

        return Response(None, status.HTTP_201_CREATED)
    
    def update(self, request, pk):        

        job = Job.objects.get(pk=pk)
        job.title = request.data['title']
        job.description = request.data['description']
        job.datetime = request.data['datetime']
        job.location = request.data['location']
        job.address = request.data['address']
        job.lat = request.data['lat']
        job.long = request.data['long']
        job.category = Skill.objects.get(pk = request.data['category'])
        
        job.save()
        
        existing_gear = JobGear.objects.filter(job = job)
        for gear in existing_gear:
            gear.delete()
        new_gear = request.data['gear']
        for gear in new_gear:
            JobGear.objects.create(gear = Gear.objects.get(pk=gear), job = job)
        
        return Response(None, status.HTTP_202_ACCEPTED)
        
    def destroy(self, request, pk):
      
        job = Job.objects.get(pk=pk)
        job.delete()
        
        return Response(None, status.HTTP_204_NO_CONTENT)
      
class JobSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Job
        fields = ('id', 'title', 'description', 'datetime', 'location',
                  'address', 'lat', 'long', 'category', 'uid')
        depth = 1
