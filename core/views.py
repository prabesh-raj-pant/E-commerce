from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth import get_user_model
from .serializers import *
from django.core.mail import send_mail

  
User=get_user_model()
# Create your views here.



@api_view(['GET','POST'])
def login(request):
    if request.method== 'POST':
        email=request.data.get('username')
        password=request.data.get('password')
        
        user=authenticate(username=email,password=password)
        
        if user:
            token,_=Token.objects.get_or_create(user=user)
            return Response({
                'user':user.get_username(),
                'token':token.key   
            })
        return Response({"detail": "Invalid credentials"}, status=400)
    return render(request,'login.html')


@api_view(['GET','POST'])
def register(request):
    if request.method=='POST':
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email=serializer.validated_data.get('email')
        password=serializer.validated_data.get('password')

        user=User.objects.create_user(email=email,password=password)

        if user:
            send_mail(
                "Welcome to E-commerce",
                "Hello"+ user.email+"Welcome to E-commerce",
                "test@gmail.com",
                [user.email],
            )
            return Response('user has been created')
        return Response("something went wrong",status=400)
    
    return render(request,'register.html')
 
    
    