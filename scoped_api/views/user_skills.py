from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scoped_api.models import UserSkill, Skill, User, Company

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
    
    def create(self, request):
        
        user = User.objects.get(pk=request.data['uid'])
        company = Company.objects.get(pk=request.data['cid'])
        
        existing_skills = UserSkill.objects.filter(user=user, company=company)
        
        for skill in existing_skills:
            skill.delete()
            
        new_skills = request.data['skills']
        
        for skill in new_skills:
            new_skill = UserSkill.objects.create(
            skill = Skill.objects.get(pk=skill),
            user = user,
            company = company
            )
            new_skill.save()
        
        return Response(None, status.HTTP_201_CREATED)
    
                      
        
          
        


class UserSkillSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = UserSkill
        fields = ['skill']
        depth = 1
