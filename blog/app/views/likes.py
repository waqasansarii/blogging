from rest_framework.viewsets import ModelViewSet

from ..serializers.like_serializer import BlogLikeSerializer,CommentLikeSerializer
from ..models import BlogLike,CommentLike


class BlogLikeView (ModelViewSet):
    queryset= BlogLike.objects.all()
    serializer_class= BlogLikeSerializer
    

class CommentLikeView (ModelViewSet):
    queryset = CommentLike.objects.all()
    serializer_class= CommentLikeSerializer    