from rest_framework.permissions import BasePermission
from rest_framework.permissions import SAFE_METHODS

class IsAdminOrNot(BasePermission):
    def has_permission(self, request, view):
       
        return request.method in SAFE_METHODS or (request.user.is_authenticated and request.user.is_superuser or request.user.is_staff)
        # if request.method in SAFE_METHODS:
        #     return True
        # if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        #     return True
        # return False


class IsOwnerOrNot(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.methond in SAFE_METHODS :
            return True
        return obj.customer.user==request.user and request.user.is_authenticated
    
    