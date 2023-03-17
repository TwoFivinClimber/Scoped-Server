from datetime import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scoped_api.models import Company, User, Employee
from .serializers import CompanyEmployeeSerializer

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
          logo = request.data['logo'],
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
        company.image = request.data['image']
        company.logo = request.data['logo']
        company.type = request.data['type']
        company.email = request.data['email'],
        company.phone = request.data['phone'],
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
        

class CompanySerializer(serializers.ModelSerializer):
    employees = CompanyEmployeeSerializer(many=True)

    class Meta:
        model = Company
        fields = ('id', 'owner', 'name', 'email', 'phone', 'image', 'logo', 'type', 'description', 'location', 'lat', 'long', 'creation', 'employees')
        depth = 1
        
        
