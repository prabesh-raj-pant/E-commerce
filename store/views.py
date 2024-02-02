from django.http import Http404
from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.

# class base view
class CategoryList(APIView):
  def get(self,request):
    categories=Category.objects.all()
    serializer=CategorySerializer(categories,many=True)
    return Response(serializer.data)
  
  def post(self,request):
    serializer=CategorySerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({
      'error':"error in creating new category",  
    },
    status=status.HTTP_201_CREATED)
  




class CategoryDetails(APIView):
  def get_object(self,pk):
    try:
      return Category.objects.get(pk=pk)
    except Category.DoesNotExist:
      raise Http404
  
  def get(self,request,pk):
    category=self.get_object(pk)
    serializer=CategorySerializer(category)
    return Response(
        serializer.data,
      )
    
  def delete(self,request,pk):
    category=self.get_object(pk)
    category.delete()
    return Response(
        status=status.HTTP_204_NO_CONTENT
      )
    
  def put(self,request,pk):
    category=self.get_object(pk)
    serializer=CategorySerializer(category,data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(
        {
          'details':'data has been updated'
        }
      )





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