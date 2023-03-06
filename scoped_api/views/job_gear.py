from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scoped_api.models import JobGear, Job, Gear

class JobGearView(ViewSet):

    def create(self, request):
      
        job = Job.objects.get(pk = request.data['jobId'])
        items = request.data['gear']
        
        for item in items:
            JobGear.objects.create(
              job = job,
              gear = Gear.objects.get(pk = item)
            )
        
        return Response(None, status.HTTP_201_CREATED)

    def update(self, request, pk):

        job = Job.objects.get(pk = pk)
        items = request.data['gear']
        
        existing_items = JobGear.objects.filter(job=job)
        for item in existing_items:
            item.delete()
        
        for item in items:
            JobGear.objects.create(
              job = job,
              gear = Gear.objects.get(pk = item)
            )
        
        return Response(None, status.HTTP_201_CREATED)

        

class JobGearSerializer(serializers.ModelSerializer):

    class Meta:

        model = JobGear
        fields = ('id', 'job', 'gear')
        depth = 1
