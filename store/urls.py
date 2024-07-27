
from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import SimpleRouter
routers=SimpleRouter()
routers.register('categories',CategoryViewset,basename='category')
routers.register('products',ProductViewset,basename='product')
routers.register('customers',CustomerViewset,basename='customer')
routers.register('carts',CartViewset,basename='cart')
routers.register('cart-items',OrderViewset,basename='cart-item')
routers.register('orders',CartItemViewset,basename='order')
routers.register('reviews',ReviewViewset,basename='review')
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)