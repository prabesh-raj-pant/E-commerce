
from django.urls import path,include
from .views import *  
from store.views import index

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/',login,name='usrlogin'),
    path('register/',register,name='register'), 
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', index, name='index'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)