from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics,viewsets
from rest_framework.decorators import action
# Create your views here.

# viewset
class CategoryViewset(viewsets.ModelViewSet):
  queryset=Category.objects.all()
  serializer_class=CategorySerializer
  
  
  

  #select_related  do join table operation
class ProductViewset(viewsets.ModelViewSet):
  queryset=Product.objects.select_related('category').all()
  serializer_class=ProductSerializer


# class base view
# class CategoryList(generics.ListCreateAPIView):
#   queryset=Category.objects.all()
#   serializer_class=CategorySerializer


# class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
#   queryset=Category.objects.all()
#   serializer_class=CategorySerializer
  
# class ProductList(generics.ListCreateAPIView):
#   queryset=Product.objects.all()
#   serializer_class=ProductSerializer

# class ProductDetails(generics.RetrieveUpdateDestroyAPIView):
#   queryset=Product.objects.all()
#   serializer_class=ProductSerializer




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