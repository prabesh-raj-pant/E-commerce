
from django.urls import path,include
from .views import *
urlpatterns = [
    # path('login',login),
    # path('register',register),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]