from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scoped_api.models import User, Skill, UserSkill
from .serializers import UserSkillsSerializer

class UserView(ViewSet):

    def list(self, request):
        crew = request.query_params.get('crew')
        users = User.objects.all()
        
        users_serialized = UserSerializer(users, many = True).data
        if crew:
            for user in users_serialized:
                user['value'] = user.pop('id')
                user['label'] = user.pop('name')
        return Response(users_serialized)
      
    def retrieve(self, request, pk):

        user = User.objects.get(pk=pk)
        
        user_serialized = UserSerializer(user).data
        user_skills = UserSkill.objects.filter(user=user)
        user_serialized['skills'] = UserSkillsSerializer(user_skills, many=True).data
        return Response(user_serialized)
      
    def update(self, request, pk):

        user = User.objects.get(pk=pk)
        user.name = request.data['name']
        user.bio = request.data['bio']
        user.save()
        
        existing_skills = UserSkill.objects.filter(user=user)
        for skill in existing_skills:
            skill.delete()
        
        new_skills = request.data['skills']
        for skill in new_skills:
            UserSkill.objects.create(user=user, skill=Skill.objects.get(pk=skill))
        
        return Response(None, status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk):

        user = User.objects.get(pk=pk)
        user.delete()

        return Response(None, status.HTTP_204_NO_CONTENT)
class UserSerializer(serializers.ModelSerializer):
    skills = UserSkillsSerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'firebase', 'name', 'bio', 'image', 'skills')
        depth = 2
