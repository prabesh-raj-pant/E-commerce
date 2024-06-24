from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from .pagination import CustomPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly,SAFE_METHODS,IsAuthenticated
from .permissions import *
from django_filters import rest_framework as filters
from rest_framework import filters as f
from .filters import ProductFilter
from django.db.models import Q,Count,Prefetch
from rest_framework import mixins
from drf_yasg.utils import swagger_auto_schema




# Create your views here.


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    
    serializer_class = CategorySerializer
    permission_classes=(
        IsAuthenticatedOrReadOnly,
        IsAdminOrNot
    )
    
    

    def get_queryset(self):
        return Category.objects.prefetch_related(
              "products"
            ) \
            .annotate(
               total_product=Count('products')
            ) \
            .all()

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category').all()
    serializer_class = ProductSerialzer
    pagination_class = CustomPagination
    filter_backends=(filters.DjangoFilterBackend,f.SearchFilter,)
    filterset_class=ProductFilter    
    search_fields=('name',)
    
    


class CustomerViewset(viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated,)
    
        
    def get_queryset(self):
        user=self.request.user
        return Customer.objects.get(user=user)
    
    
    def list(self, request, *args, **kwargs):
        customer=self.get_queryset()
        serializer = self.serializer_class(customer)
        return Response(serializer.data)
    
    
    def update(self,request,*args,**kwargs):
        
        customer=self.get_queryset()
        context={}
        context['request']=request
        serializer = self.serializer_class(data=request.data,instance=customer,context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
    
    # @action(methods=('get'),detail=True)
    # def me(self):
    #     return Response('ok')
    
    
    

class CartViewset(viewsets.ViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerailizer
    pagination_class = CustomPagination
    permission_classes=(IsAuthenticated,)

    
    def list(self,request,*args,**kwargs):
        customer=Customer.objects.filter(user=self.request.user).first()
        cart,_=Cart.objects.prefetch_related('items').get_or_create(customer=customer)
        serializer=CartSerailizer(cart)
        return Response(serializer.data)

class CartItemViewset(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_class=(IsAuthenticated,)
    
    def get_queryset(self):
        customer=Customer.objects.filter(user=self.request.user).first()
        cart,_=Cart.objects.prefetch_related('items').get_or_create(customer=customer)
        
        return CartItem.objects.filter(
            cart=cart
        )



class OrderViewset(viewsets.ModelViewSet):
    queryset=Order.objects.prefetch_related('order_items').all()
    serializer_class=OrderSerializer
    permission_classes=[
        IsAuthenticated,
    ]
    
    
    def get_queryset(self):
        return Order.objects.prefetch_related('order_items').filter(
            customer__user=self.request.user
        )
        
    def get_serializer_class(self):
        if self.request.method == "PUT":
            return CancelOrderSerializer
        return OrderSerializer
    
    
    

class ReviewViewset(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes=(
        IsAuthenticated,
        IsOwnerOrNot,
    )
    
    
    
        