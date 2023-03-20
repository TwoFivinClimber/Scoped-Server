from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scoped_api.models import Skill, Company


class SkillsView(ViewSet):

    def list(self, request):
        
        cid = request.query_params.get('cid')
        if cid is not None:
            skills = Skill.objects.filter(company = cid)
        
        skills_serialized = SkillsSerializer(skills, many=True).data
        
        for skill in skills_serialized:
            skill['value'] = skill.pop('id')
            skill['label'] = skill.pop('skill')
            
        return Response(skills_serialized, status.HTTP_200_OK)
    
    def create(self, request): 
        
        skill = Skill.objects.create(
            skill = request.data['skill'],
            company = Company.objects.get(pk = request.data['cid'])
        )
        
        skill_serialized = SkillsSerializer(skill).data
        
        return Response(skill_serialized,  status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        
        skill = Skill.objects.get(pk=pk)
        skill.delete()

        return Response(None, status.HTTP_204_NO_CONTENT)
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Skill
        fields= ('id', 'skill')
