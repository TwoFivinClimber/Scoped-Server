from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from scoped_api.models import User
from scoped_api.views.users import UserSerializer


@api_view(['POST'])
def check_user(request):
    '''checks if user has created profile'''
    uid = request.data['uid']
    try :
        user = User.objects.get(firebase = uid)
        
        user_serialized = UserSerializer(user).data
        
        return Response(user_serialized, status.HTTP_200_OK)

    except: 
        data = { 'valid': False }
        return Response(data)
      
@api_view(['POST'])
def register_user(request):
    '''handels creation of new user'''
    
    user = User.objects.create(
      firebase=request.data['firebase'],
      name=request.data['name'],
      phone=request.data['phone'],
      email=request.data['email'],
      bio=request.data['bio'],
      image=request.data['image']
    )
        
    
    data = {
      'id': user.id,
      'name': user.name,
    }
    
    return Response(data)
          
        
    
