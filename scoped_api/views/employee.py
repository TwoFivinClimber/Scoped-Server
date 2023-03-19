from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scoped_api.models import Employee, UserSkill
from .user_skills import UserSkillSerializer

class EmployeeView(ViewSet):

    def list(self, request):

        company = request.query_params.get('cid')
        
        if company is not None:
            employees = Employee.objects.filter(company = company)
            
            for emp in employees:
                emp.skills = UserSkill.objects.filter(user=emp.pk, company = company)
        
        employees_serialized = EmployeeSerializer(employees, many=True).data
        
        return Response(employees_serialized, status.HTTP_200_OK)
    
class EmployeeSerializer(serializers.ModelSerializer):
    skills = UserSkillSerializer(many=True)
    class Meta:
        model = Employee
        fields = ('id', 'admin', 'user', 'creation', 'skills')
        depth = 1
        
