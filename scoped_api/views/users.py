from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scoped_api.models import User, Skill


class UserView(ViewSet):

    def retrieve(self, request, pk):

        user = User.objects.get(pk=pk)
        
        user_serialized = UserSerializer(user)
        
        return Response(user_serialized.data)
        

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'firebase', 'name', 'bio', 'image')
