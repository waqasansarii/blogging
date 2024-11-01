from django.db import transaction
from rest_framework.response import Response
from rest_framework import serializers
from ..models import Blog,Category,User,Comments,BlogLike
from .user_serializer import UserSerializer
from .category_serializer import CategorySerializer
# from .comment_serializer import 

# class CommentSerializer(serializers.ModelSerializer):
#     # user = UserSerializer(read_only=True)
#     class Meta:
#         model = Comments
#         fields=['id','content','user','created_at']



class BlogSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)
    contributors= UserSerializer(read_only=True,many=True)
    category = CategorySerializer(read_only=True,many=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        many=True,
        write_only=True
        )
    contributors_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.filter(roles__in=[2]).all(),
        many=True,
        write_only=True
        )
    # comments = CommentSerializer(read_only=True,source='comment_blog',many=True)
    comments = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog
        fields = ['id','title','content','author','contributors','category','category_id',
                  'contributors_id','comments','likes','created_at'
                  ]
        read_only_fields = ['author']
    
    
    def get_comments(self,obj):
        return obj.comment_blog.count()
    
    # count total likes using related_name 
    def get_likes(self,obj ): # obj is Blog instance and get__+(name which define above with SerializerMethodField)
        return obj.likes_blog.count() #likes_blog is related_name
    
    
    # override create method to add category and contributors in intermediate table 
    def create(self, validated_data):
        try:
            with transaction.atomic():
                contributors = validated_data.pop('contributors_id')
                category = validated_data.pop('category_id')
                validated_data['author'] = self.context['request'].user
                blog = Blog.objects.create(**validated_data)
                blog.contributors.set(contributors)
                blog.category.set(category)
        
            return blog  
        except Exception as e:
            return e
        # Response({'status': 'error', 'message': str(e)}, status=400)

    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        # print('validated data',validated_data)
        
        if  len(validated_data['contributors_id'])>0:
            contributors = validated_data.pop('contributors_id')
            instance.contributors.set(contributors) 
             
        if  len(validated_data['category_id'])>0 :
            categories = validated_data.pop('category_id')
            instance.category.set(categories)  

        instance.save()
        
        return instance
        

        