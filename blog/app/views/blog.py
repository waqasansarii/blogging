# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# from 
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from ..serializers.blog_serializer import BlogSerializer
from ..models import Blog
from ..permission import IsAuthorOrReadOnly,IsAuthorOrModerator


# @permission_classes([IsAuthorOrModerator])
class BlogView(ModelViewSet):
    queryset =  Blog.objects.select_related('author').prefetch_related('contributors','category').all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly,IsAuthorOrModerator]
    
    def get_queryset(self):
        if self.request.user.roles ==0 or self.request.user.is_staff:
            queryset = self.queryset.all()
            return queryset
            
            
        queryset = self.queryset.filter(author = self.request.user).all()
        return queryset
        # return super().get_queryset()
    # def list(self, request, *args, **kwargs):
    #     return super().list(request, *args, **kwargs)
    
    
 
