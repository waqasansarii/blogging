from rest_framework import serializers
from ..models import BlogLike,CommentLike


class BlogLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogLike
        fields ='__all__'
        
        
class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields ='__all__'        
