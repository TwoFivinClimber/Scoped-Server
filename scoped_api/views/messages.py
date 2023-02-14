from datetime import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scoped_api.models import Message, Job, User


class MessageView(ViewSet):
  
    def list(self, request):

        job = request.query_params.get('job')
        if job is not None:
            messages = Message.objects.filter(job=job)
        
        messages_serialized = MessageSerializer(messages, many=True)
        
        return Response(messages_serialized.data)
    
    def create(self, request):
        
        message = Message.objects.create(
            content = request.data['content'],
            datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            job = Job.objects.get(pk = request.data['job']),
            uid = User.objects.get(pk = request.data['uid'])
        )
        message.save()
        
        return Response(None, status.HTTP_201_CREATED)
    
    def update(self,request,pk):
        
        message = Message.objects.get(pk=pk)
        message.content = request.data['content']
        message.datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message.save()
        
        return Response(None, status.HTTP_202_ACCEPTED)
    
    def destroy(self,request,pk):
        
        message = Message.objects.get(pk=pk)
        message.delete()
        
        return Response(None, status.HTTP_204_NO_CONTENT)
        
class MessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Message
        fields = ('id', 'content', 'datetime', 'job', 'uid')
        
