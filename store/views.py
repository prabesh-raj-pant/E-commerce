from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import viewsets
from .pagination import CustomPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import *
from django_filters import rest_framework as filters
from rest_framework import filters as f
from .filters import ProductFilter
from django.db.models import Q,Count,Prefetch
# Create your views here.

# viewset
class CategoryViewset(viewsets.ModelViewSet):
  queryset=Category.objects.all()
  
  serializer_class=CategorySerializer
  permission_classes=(
    IsAuthenticatedOrReadOnly,
    IsAdminOrNot,
  )
  def get_queryset(self):
    return Category.objects.prefetch_related(
           "products"
      ) \
      .annotate(
        total_product=Count('products')
    )\
  .all()
  
  
  

  #select_related  do join table operation
class ProductViewset(viewsets.ModelViewSet):
  queryset=Product.objects.select_related('category').all()
  serializer_class=ProductSerializer
  pagination_class=CustomPagination
  filter_backends=(filters.DjangoFilterBackend,f.SearchFilter)
  filterset_class=ProductFilter
  SearchFilter=('name',)
  
  
# class Customer(viewsets.ModelViewSet):
#   queryset=Customer.objects.all()
#   serializer_class=CustomerSerializer
  
class CustomerViewset(viewsets.GenericViewSet):
  queryset=Customer.objects.all()
  serializer_class=CustomerSerializer
  permission_classes=(IsAuthenticatedOrReadOnly,)

  
  
  def get_queryset(self):
    user=self.request.user
    return Customer.objects.get(user=user)
  
  def list(self,request,*args,**kwargs):
    customer=self.get_queryset().first()
    serializer=self.serializer_class(customer)
    return Response(serializer.data)

    
  def update(self,request,*args,**kwargs):
    customer=self.get_queryset()
    context={}
    context['request']=request
    serializer=self.serializer_class(data=request.data,instance=customer,context=context)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  
  
class CartViewset(viewsets.ViewSet):
  queryset=Cart.objects.all()
  serializer_class=CartSeraillizer
  pagination_class=CustomPagination
  permission_classes=(IsAuthenticatedOrReadOnly,)
  
  def list(self,reques,*args,**kwargs):
    customer=Customer.objects.filter(user=self.request.user).first()
    cart,_=Cart.objects.prefetch_related('items').get_or_create(customer=customer)
    serializer=CartSeraillizer(cart)
    return Response(serializer.data)
  

class CartItemViewset(viewsets.ModelViewSet):
  queryset=CartItem.objects.all()
  serializer_class=CartItemSerializer
  pagination_class=CustomPagination
  authentication_classes=(IsAuthenticatedOrReadOnly,)
  def get_queryset(self):
    customer=Customer.objects.filter(user=self.request.user).first()
    cart,_=Cart.objects.prefetch_related('items').get_or_create(customer=customer)
    return CartItem.objects.filter(
      cart=cart
    )
  

class OrderViewset(viewsets.ModelViewSet):
  queryset=Order.objects.all()
  serializer_class=OrderSerializer
  permission_classes=[
    IsAuthenticatedOrReadOnly,
  ]
  
  def  get_queryset(self):
     
    return Order.objects.filter(
        customer__user=self.request.user
      )
  
  def get_serializer_class(self):
    if self.request.method == "PUT":
      return CancelOrderSerializer
    return OrderSerializer
  
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