from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scoped_api.models import Skill


class SkillsView(ViewSet):

    def list(self, request):
      
        skills = Skill.objects.all()
        
        skills_serialized = SkillsSerializer(skills, many=True).data
        
        for skill in skills_serialized:
            skill['value'] = skill.pop('id')
            skill['label'] = skill.pop('skill')
            
        return Response(skills_serialized, status.HTTP_200_OK)

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Skill
        fields= ('id', 'skill')
