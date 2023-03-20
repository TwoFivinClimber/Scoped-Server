from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from scoped_api.models import Gear, Company

class GearView(ViewSet):
  
    def list(self, request):

        cid = request.query_params.get('cid')
        if cid is not None:
            gear = Gear.objects.filter(company = cid)
        
        gear_serialized = GearSerializer(gear, many=True).data
        for item in gear_serialized:
            item['value'] = item.pop('id')
            item['label'] = item.pop('name')
            
        return Response(gear_serialized, status.HTTP_200_OK)
    
    def create(self, request):
        
        item = Gear.objects.create(
            name = request.data['name'],
            company = Company.objects.get(pk=request.data['cid'])
        )
        
        gear_serialized = GearSerializer(item).data
        
        return Response(gear_serialized, status.HTTP_201_CREATED)
        
    def destroy(self, request, pk):
        
        item = Gear.objects.get(pk=pk)
        item.delete()
        
        return Response(None, status.HTTP_204_NO_CONTENT)

        

class GearSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gear
        fields = ('id', 'name', 'company')
