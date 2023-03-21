from datetime import datetime
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from scoped_api.models import Invite, User, Company, Employee
from .employee import EmployeeSerializer

class InviteView(ViewSet):
  
    def list(self, request):

        cid = request.query_params.get('cid')
        uid = request.query_params.get('uid')
        if cid is not None:
            invites = Invite.objects.filter(company = cid)

        if uid is not None:
            invites = Invite.objects.filter(uid = uid)
            
        invites_serialized = InviteSerializer(invites, many=True).data
        
        return Response(invites_serialized, status.HTTP_200_OK)
      
    def create(self, request):

        invite = Invite.objects.create(
          uid = User.objects.get(pk = request.data['uid']),
          company = Company.objects.get(pk = request.data['cid'])
        )
        invite.save()
        
        invite_serialized = InviteSerializer(invite).data
        
        return Response(invite_serialized, status.HTTP_201_CREATED)
    
    def destroy(self, request, pk):
        
        invite = Invite.objects.get(pk=pk)
        invite.delete()
        
        return Response(None, status.HTTP_204_NO_CONTENT)
    
    @action(methods=['post'], detail=True)
    def employ(self, request, pk):
        try:
            invite = Invite.objects.get(pk=pk)
            employee = Employee.objects.create(
                company = Company.objects.get(pk = invite.company_id),
                user = User.objects.get(pk=invite.uid_id),
                creation = datetime.now().strftime("%Y-%m-%d")
            )
            employee.save()
            invite.delete()
            return Response(None, status.HTTP_201_CREATED)
        except Invite.DoesNotExist as ex:
            return Response(ex, status.HTTP_404_NOT_FOUND)
        
    @action(methods=['delete'], detail=True)
    def deny(self, request, pk):
        try:
            invite = Invite.objects.get(pk=pk)
            invite.delete()
            
            return Response(None, status.HTTP_204_NO_CONTENT)
        
        except Invite.DoesNotExist as ex:
            return Response(ex, status.HTTP_404_NOT_FOUND )
            
            
    

class InviteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invite
        fields = ('id', 'uid', 'company')
        depth = 2
