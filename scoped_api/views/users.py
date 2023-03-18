from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scoped_api.models import User, Skill, UserSkill, Crew, Employee
from .serializers import UserSkillsSerializer, UserJobSerializer, UserCompanySerializer

class UserView(ViewSet):

    def list(self, request):
        job = request.query_params.get('job')
        company = request.query_params.get('cid')
        
        users = User.objects.all()
        if job is not None:
            crews = Crew.objects.filter(job=job)
            users = users.exclude(pk__in=crews.values_list('uid', flat=True))
        
        if company is not None:
            employees = Employee.objects.filter(company = company)
            print(len(employees))
            
            users = users.exclude(pk__in=employees.values_list('user_id'))

            
        users_serialized = UserSerializer(users, many = True).data
        for user in users_serialized:
            user['value'] = user.pop('id')
            user['label'] = user.pop('name')


        for user in users_serialized:
            for skill in user['skills']:
                skill['skill']['value'] = skill['skill'].pop('id')
                skill['skill']['label'] = skill['skill'].pop('skill')

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
        user.phone = request.data['phone']
        user.email = request.data['email']
        user.bio = request.data['bio']
        user.save()
        
        existing_skills = UserSkill.objects.filter(user=user)
        for skill in existing_skills:
            skill.delete()
        
        new_skills = request.data['skills']
        for skill in new_skills:
            UserSkill.objects.create(user=user, skill=Skill.objects.get(pk=skill))
        
        user_serialized = UserSerializer(user).data
        
        return Response(user_serialized, status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk):

        user = User.objects.get(pk=pk)
        user.delete()

        return Response(None, status.HTTP_204_NO_CONTENT)
class UserSerializer(serializers.ModelSerializer):
    skills = UserSkillsSerializer(many=True)
    jobs = UserJobSerializer(many=True)
    companies = UserCompanySerializer(many=True)
    class Meta:
        model = User
        fields = ('id', 'firebase', 'name', 'phone', "email", 'bio', 'image', 'skills', 'jobs', 'companies')
        depth = 2
