from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAuthorOrModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.roles == 0:
                return request.method in SAFE_METHODS
        
            return request.user.roles in [1,2]
            


class IsAuthorOrReadOnly(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request in SAFE_METHODS:
            return True
        return request.user == obj.author or request.user in obj.contributors
