from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth import get_user_model
from .serializers import *
User=get_user_model()
# Create your views here.



@api_view(['POST'])
def login(request):
    username=request.data.get('username')
    password=request.data.get('password')
    
    user=authenticate(username=username,password=password)
    
    if user:
        token,_=Token.objects.get_or_create(user=user)
        return Response({
            'user':user.get_username(),
            'token':token.key   
        })
    return Response("invalid")


@api_view(['POST'])
def register(request):
    serializer=UserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    email=serializer.validated_data.get('email')
    password=serializer.validated_data.get('password')

    user=User.objects.create_user(email=email,password=password)

    if user:
        return Response('user has been created')
    return Response("something went wrong")
    
    
    