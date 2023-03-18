from datetime import datetime
import boto3
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from scoped_api.models import Company, User, Employee
from .serializers import CompanyEmployeeSerializer, CompanySkillsSerializer

s3 = boto3.resource('s3')
bucket = s3.Bucket('projectscoped')
bucket_name = 'projectscoped'
class CompanyView(ViewSet):
  
    def list(self, request):
  
        companies = Company.objects.all()
        
        companies_serialized = CompanySerializer(companies, many=True).data
        
        return Response(companies_serialized, status.HTTP_200_OK)
      
    def retrieve(self, request, pk):

        company = Company.objects.get(pk=pk)
        
        company_serialized = CompanySerializer(company).data
        
        return Response(company_serialized, status.HTTP_200_OK)
    
    def create(self, request):
        
        company = Company.objects.create(
          owner = User.objects.get(pk = request.data['uid']),
          name = request.data['name'],
          type = request.data['type'],
          email = request.data['email'],
          phone = request.data['phone'],
          description = request.data['description'],
          location = request.data['location'],
          lat = request.data['lat'],
          long = request.data['long'],
          creation = datetime.now().strftime("%Y-%m-%d")
        )
        company.save()
        
        Employee.objects.create(
            company = company,
            user = User.objects.get(pk=request.data['uid']),
            admin = True,
            creation = datetime.now().strftime("%Y-%m-%d")
        )
        
        company_serialized = CompanySerializer(company).data
        
        return Response(company_serialized, status.HTTP_201_CREATED)
    
    def update(self, request, pk):

        
        company = Company.objects.get(pk=pk)
        company.name = request.data['name']
        company.type = request.data['type']
        company.email = request.data['email']
        company.phone = request.data['phone']
        company.description = request.data['description']
        company.location = request.data['location']
        company.lat = request.data['lat']
        company.long = request.data['long']
        company.save()
        
        return Response(None, status.HTTP_202_ACCEPTED)
    
    def destroy(self, request, pk):

        company = Company.objects.get(pk=pk)
        company.delete()
        
        return Response(None, status.HTTP_204_NO_CONTENT)
    
    @action(methods=['put'], detail=True)
    def logoadd(self, request, pk):
        try:
            company = Company.objects.get(pk=pk)
            existing_logo = company.logo
            if existing_logo is not None:
                key = str(existing_logo).split('/')[3]
                s3.Object(bucket_name, key).delete()
            company.logo = request.data['logo']
            company.save() 
            
            return Response({'message': 'Logo Updated'}, status.HTTP_202_ACCEPTED)       
        except Company.DoesNotExist:
            return Response({'message': 'Company Does not exist'}, status.HTTP_404_NOT_FOUND)
class CompanySerializer(serializers.ModelSerializer):
    employees = CompanyEmployeeSerializer(many=True)
    company_skills = CompanySkillsSerializer(many=True)

    class Meta:
        model = Company
        fields = ('id', 'owner', 'name', 'email', 'phone', 'image', 'logo', 'type', 'description', 'location', 'lat', 'long', 'creation', 'employees', 'company_skills')
        depth = 1
        
        
