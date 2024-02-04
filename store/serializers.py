from rest_framework import serializers
from .models import *
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=['id','name'] 
        
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['name','quantity','price','discounted_price','category']
    