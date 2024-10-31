# from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# from 
from rest_framework.viewsets import ModelViewSet
from ..serializers.blog_serializer import BlogSerializer
from ..models import Blog


class BlogView(ModelViewSet):
    queryset =  Blog.objects.select_related('author').prefetch_related('contributors','category').all()
    serializer_class = BlogSerializer
    
 
