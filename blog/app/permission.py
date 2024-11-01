from rest_framework.permissions import BasePermission, SAFE_METHODS
from .serializers.blog_serializer import BlogSerializer
from .serializers.user_serializer import UserSerializer

class IsAuthorOrModerator(BasePermission):
    
    def has_permission(self, request, view):
        
        if request.user.is_authenticated:
            # roles = 0 reader 
            # if request.user.roles == 0:
            if request.user.roles in [1,2]:
                # roles = 1 (moderator) and moderator cannot create and delete blogs 
                if request.method in ['POST','DELETE'] and request.user.roles == 1:
                    return False
                # only authors have full access 
                return True    
            # return request.user.roles in [1,2]
        return request.method in SAFE_METHODS
            
        # return False    


class IsAuthorOrReadOnly(BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # data = UserSerializer(obj.contributors)
        # print(data.data)
        # for key in data.data:
        #     print(data.data['contributors'])
        # print('cont',  request.user in obj.contributors)
        if request in SAFE_METHODS:
            return True
        if request.user.is_authenticated:
            return request.user == obj.author or request.user.roles == 1
        return True
