from rest_framework import serializers
from scoped_api.models import JobGear, Crew, UserSkill, Image, Job, Employee, Skill


class JobGearSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobGear
        fields = ('id', 'gear')
        depth = 1
        
class JobCrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ('id', 'accepted', 'skill', 'uid')
        depth = 1

class UserSkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkill
        fields = ('id', 'skill')
        depth = 1
        
class JobImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Image
        fields = ('id', 'image', 'description')
        
class EditJobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('id', 'title', 'description', 'datetime', 'location',
                  'address', 'lat', 'long', 'category', 'uid',)
        depth = 1

class UserJobSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Job
        fields = ('id', 'title', 'description', 'datetime', 'location',
                  'address', 'lat', 'long', 'category', 'uid',)

class UserCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'company', 'admin')
        depth = 1
        
class CompanyEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'user')
        depth = 1
class CompanySkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = 'id', 'skill'
        