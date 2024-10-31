from rest_framework import serializers
from ..models import Blog,Category,User
from .user_serializer import UserSerializer
from .category_serializer import CategorySerializer
# from .comment_serializer import CommentSerializer


class BlogSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)
    contributors= UserSerializer(read_only=True,many=True)
    category = CategorySerializer(read_only=True,many=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),many=True,write_only=True)
    contributors_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),many=True,write_only=True)
    class Meta:
        model = Blog
        fields = ['id','title','content','author','contributors','category','category_id',
                  'contributors_id','created_at'
                  ]
        read_only_fields = ['author']
    
    def create(self, validated_data):
        contributors = validated_data.pop('contributors_id')
        category = validated_data.pop('category_id')
        validated_data['author'] = self.context['request'].user
        blog = Blog.objects.create(**validated_data)
        blog.contributors.set(contributors)
        blog.category.set(category)
        return blog    
        

        