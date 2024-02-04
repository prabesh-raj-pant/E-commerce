
from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter
routers=SimpleRouter()
routers.register('categories',CategoryViewset,basename='category')
routers.register('products',ProductViewset,basename='product')
urlpatterns = [
    # path('categories',CategoryViewset.as_view({
    #     'get':'list',
    #     'post':'create'
    #     })),
    # path('categories/<pk>',CategoryViewset.as_view({
    #     'get':'retrieve',
    #     'put':'update',
    #     'delete':'destroy'
    #     })),
    
]+routers.urls
