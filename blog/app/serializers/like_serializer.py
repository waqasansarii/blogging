from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import BlogLike,CommentLike


class BlogLikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogLike
        fields ='__all__'
        read_only_fields=['user']
        
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        isLiked = BlogLike.objects.filter(user=validated_data['user'],blog = validated_data['blog']).exists()
        
        if isLiked:
            raise ValidationError("You have already liked this blog.")
 
        return super().create(validated_data)    
        
        
class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields ='__all__'    
        read_only_fields=['user']
        
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        isLiked = CommentLike.objects.filter(user=validated_data['user'],blog = validated_data['comment']).exists()
        
        if isLiked:
            raise ValidationError("You have already liked this comment.")
 
        return super().create(validated_data)    
