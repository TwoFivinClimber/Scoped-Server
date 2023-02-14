from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from scoped_api.models import Gear

class GearView(ViewSet):
  
    def list(self, request):

        gear = Gear.objects.all()
        
        gear_serialized = GearSerializer(gear, many=True).data
        for item in gear_serialized:
            item['value'] = item.pop('id')
            item['label'] = item.pop('name')
            
        return Response(gear_serialized)

class GearSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gear
        fields = ('id', 'name')
