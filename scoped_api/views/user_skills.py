from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from scoped_api.models import UserSkill

class UserSkillView(ViewSet):
  
    def list(self, request):

        uid = request.query_params.get('uid')
        if uid is not None:
            skills = UserSkill.objects.filter(user = uid)
            
        skills_serialized = UserSkillSerializer(skills, many=True).data
        
        output = []
        for skill in skills_serialized:
            skill = skill["skill"]
            output.append({"value": skill["id"], "label": skill["skill"]})
                      
        return Response(output)
          
        


class UserSkillSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = UserSkill
        fields = ['skill']
        depth = 1
