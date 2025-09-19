from rest_framework.permissions import BasePermission, IsAuthenticated


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        return obj.assigned_to == request.user
