
from django.urls import path
from .views import *
urlpatterns = [
    path('categories',CategoryList.as_view()),
    path('categories/<pk>',CategoryDetails.as_view()),
    path('products',ProductList.as_view()),
    path('products/<pk>',ProductDetails.as_view()),
]
