from rest_framework import serializers

from .user_serializer import UserSerializer
from ..models import Comments


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comments
        fields=['id','content','user','blog','created_at']
        read_only_fields=['user']
        
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)    


