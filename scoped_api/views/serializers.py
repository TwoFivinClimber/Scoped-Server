from rest_framework import serializers
from scoped_api.models import JobGear, Crew, UserSkill


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
