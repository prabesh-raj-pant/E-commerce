
from django.urls import path,include
from .views import *  
urlpatterns = [
    path('login/',login,name='usrlogin'),
    path('register/',register,name='register'), 
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]