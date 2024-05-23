from rest_framework import serializers
from .models import *
class CategorySerializer(serializers.ModelSerializer):
    total_product=serializers.IntegerField()
    class Meta:
        model=Category
        fields=('id','name','total_product')
        
    # def get_total_product(self,category:Category):
    #     return category.products.count()
    
class SimpleCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields=('id','name')
        
              
class ProductSerializer(serializers.ModelSerializer):
    price_with_tax=serializers.SerializerMethodField()
    category_id=serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),source='category'
    )
    category=SimpleCategorySerializer(read_only=True)

    class Meta:
        model=Product
        fields=(
            'name',
            'quantity',
            'price',
            'discounted_price',
            'price_with_tax',
            'category_id',
            'category'
            )
    def get_price_with_tax(self,product:Product):
        return (product.discounted_price*0.13+product.discounted_price)
    



class CustomerSerializer(serializers.ModelSerializer):
    user=serializers.HiddenField(default=serializers.CurrentUserDefault)
    first_name=serializers.CharField(required=True)
    middle_name=serializers.CharField(required=True)
    last_name=serializers.CharField(required=True)
    address=serializers.CharField(required=True)
    gender=serializers.ChoiceField(required=True,choices=Customer.GENDER_CHOICES)
    class Meta:
        model=Customer
        fields="__all__"


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields="__all__"
        
        
        
        
class CartItemSerializer(serializers.ModelSerializer):
    product_id=serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source= "product"
    )
    product=ProductSerializer(read_only=True)
    class Meta:
        model=CartItem
        fields=[
            'id',
            'product_id',   
            'quantity',
            'product',
        ]
        def create(self,validated_data):
            request=self.contex['request']
            cart= Cart.objects.get(customer__ser=request.user)
            validated_data.update({
                'cart':cart
            })
            return super().create(validated_data)



class CartSeraillizer(serializers.ModelSerializer):
    
    customer=serializers.StringRelatedField()
    customer_id=serializers.PrimaryKeyRelatedField(
            queryset=Customer.objects.all(),
            source='customer'
        )
    items=CartItemSerializer(many=True)
    class Meta:
        model=Cart
        fields="__all__"

