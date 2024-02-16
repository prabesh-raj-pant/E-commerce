from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

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
