from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from scoped_api.models import Crew, Skill, User, Job


class CrewView(ViewSet):

    def list(self, request):

        crew = Crew.objects.all()
        
        job = request.query_params.get('job')
        uid = request.query_params.get('uid')
        
        
        if job is not None:
            crew = crew.filter(job = job)
        if uid is not None:
            crew = crew.filter(uid = uid, accepted = None)
        
        crew_serialized = CrewSerializer(crew, many=True).data
        
        return Response(crew_serialized)
    
    def create(self, request):
        
        
        
        crew_member = Crew.objects.create(
           job = Job.objects.get(pk = request.data['job']),
           skill = Skill.objects.get(pk = request.data['skill']),
           uid = User.objects.get(pk = request.data['uid'])
        )
        crew_member.save()
        
        return Response(None, status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        
        crew_member = Crew.objects.get(pk=pk)
        
        crew_member.skill = Skill.objects.get(pk = request.data['skill'])
        crew_member.save()
        
        return Response(None, status.HTTP_204_NO_CONTENT)
      
    
    def destroy(self, request, pk):

        crew_member = Crew.objects.get(pk=pk)
        crew_member.delete()
        
        return Response(None, status.HTTP_204_NO_CONTENT)
    
    @action(methods=['put'], detail=True)
    def accept(self, request, pk):
        try:
            crew = Crew.objects.get(pk=pk, accepted=None)
            crew.accepted = True
            crew.save()
        
            return Response({'message': 'Job Accepted'}, status.HTTP_202_ACCEPTED)
          
        except Crew.DoesNotExist:
            return Response({'message': 'Job has already been accepted or declined'}, status.HTTP_403_FORBIDDEN)
    
    @action(methods=['put'], detail=True)
    def decline(self, request, pk):

        try:
            crew = Crew.objects.get(pk=pk, accepted = None)
            crew.accepted = False
            crew.save()
        
            return Response({'message': 'Job Declined'}, status.HTTP_202_ACCEPTED)
        
        except Crew.DoesNotExist:
            return Response({'message': 'Job has already been accepted or declined'}, status.HTTP_403_FORBIDDEN)
          
    @action(methods=['put'], detail=True)
    def re_send(self, request, pk):

        crew = Crew.objects.get(pk=pk)
        crew.accepted = None
        crew.save()
        
        return Response({'message': 'Job request re-sent'}, status.HTTP_200_OK)
      

class CrewSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = Crew
        fields = ('id', 'accepted', 'skill', 'uid', 'job')
        depth = 2        
