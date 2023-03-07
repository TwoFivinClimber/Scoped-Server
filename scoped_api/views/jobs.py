import boto3
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scoped_api.models import Job, Skill, User, JobGear, Gear, Crew, Image
from .serializers import JobGearSerializer, JobCrewSerializer, JobImageSerializer

s3 = boto3.resource('s3')
bucket = s3.Bucket('projectscoped')
bucket_name = 'projectscoped'

class JobView(ViewSet):
  
    def list(self, request):
      
        jobs = Job.objects.all()
        
        uid = request.query_params.get('uid')
        
        if uid is not None:
            user_jobs = Crew.objects.filter(uid=uid)
            jobs =[job for job in jobs for user_job in user_jobs if user_job.job == job]
            
            for job in jobs:
                job.accepted = Crew.objects.get(job = job, uid = uid).accepted
        
        jobs_serialized = JobSerializer(jobs, many=True)
        
        return Response(jobs_serialized.data)
    
    def retrieve(self, request, pk):

        job = Job.objects.get(pk=pk)
        
        job_serialized = JobSerializer(job).data
        job_gear = JobGear.objects.filter(job=job)
        job_crew = Crew.objects.filter(job=job)
        job_images = Image.objects.filter(job=job)
        job_serialized['gear'] = JobGearSerializer(job_gear, many=True).data
        for obj in job_serialized['gear']:
            obj['gear']['value'] = obj['gear'].pop('id')
            obj['gear']['label'] = obj['gear'].pop('name')
        job_serialized['crew'] = JobCrewSerializer(job_crew, many=True).data
        job_serialized['images'] = JobImageSerializer(job_images, many=True).data
        
        
        return Response(job_serialized)
    
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
        
        job_serialized = JobSerializer(job).data

        return Response(job_serialized, status.HTTP_201_CREATED)
    
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
        images = Image.objects.filter(job = job)
        
        for image in images:
            key = str(image.image).split('/')[3]
            s3.Object(bucket_name, key).delete()
        
        job.delete()
        
        return Response(None, status.HTTP_204_NO_CONTENT)
      
class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('id', 'title', 'description', 'datetime', 'location',
                  'address', 'lat', 'long', 'category', 'uid', 'crew', 'messages', 'gear', 'accepted', 'images')
        depth = 1
        
