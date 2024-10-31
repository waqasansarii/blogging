from rest_framework import serializers
from ..models import Blog,Category,User
from .user_serializer import ProfileSerializer
from .category_serializer import CategorySerializer


class BlogSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(queryset = User.objects.all(),read_only=True)
    # author = ProfileSerializer(read_only=True)
    contributors=ProfileSerializer(read_only=True,many=True)
    category = CategorySerializer(read_only=True,many=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),many=True,write_only=True)
    contributors_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=True,write_only=True)
    class Meta:
        model = Blog
        fields = ['id','title','content','author','contributors','category','category_id','contributors_id','created_at']
        read_only_fields = ['author']
        
        