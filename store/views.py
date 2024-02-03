from django.http import Http404
from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
# Create your views here.

# class base view
class CategoryList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
  queryset=Category.objects.all()
  serializer_class=CategorySerializer
  
  def get(self,request):
    return self.list(request)
  
  def post(self,request):
    return self.create(request)
  
  


class CategoryDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
  queryset=Category.objects.all()
  serializer_class=CategorySerializer
  
  def get(self,request,*args,**kwargs):
    return self.retrieve(request,*args,**kwargs)
    
  def delete(self,request,*args,**kwargs):
    return self.destroy(request,*args,**kwargs)
    
  def put(self,request,*args,**kwargs):
    return self.update(request,*args,**kwargs)





# functional base view...........


# @api_view(['GET','POST'])
# def category_list(request):
#     if request.method=='GET':
#       categories=Category.objects.all()
#       serializer=CategorySerializer(categories,many=True)
#       return Response(serializer.data)
#     else:
#       serializer=CategorySerializer(data=request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response({
#         'error':"error in creating new category",  
#       },
#       status=status.HTTP_201_CREATED)
 
 
# TO BACKUP
# python3 manage.py -Xutf8 dumpdate > backup.json
# to load data back into database
# python3 manage.py loaddata backup.json
 
        
# @api_view(['GET','DELETE','PUT'])     
# def category_detail(request,pk):
#     category=get_object_or_404(Category,pk=pk)
#     if request.method=="GET": 
#       serializer=CategorySerializer(category)
#       return Response(
#         serializer.data,
#       )
#     if request.method=="DELETE":
#       category.delete()
#       return Response(
#         status=status.HTTP_204_NO_CONTENT
#       )
#     if request.method=="PUT":
#       serializer=CategorySerializer(category,data=request.data)
#       serializer.is_valid(raise_exception=True)
#       serializer.save()
#       return Response(
#         {
#           'details':'data has been updated'
#         }
#       )