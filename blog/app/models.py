from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    username = None
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['first_name','last_name']
    dob = models.DateField(null=True,blank=True)
    
    roles_choices = [
        (0,'reader'),
        (1,'moderator'),
        (2,'author')
    ]
    roles = models.IntegerField(choices=roles_choices,default=0)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Category(models.Model):
    name = models.CharField(max_length=30,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name 


class Blog(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.ForeignKey(User,related_name='blog_author',on_delete=models.CASCADE)
    contributors = models.ManyToManyField(User,related_name='blog_contributor')
    category = models.ManyToManyField(Category,related_name='blog_category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.title 
            
            
class Comments(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User,related_name='comment_user',on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog,related_name='comment_blog',on_delete=models.CASCADE)            
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    

class BlogLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes_user_blog")
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="likes_blog")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'blog')  

    def __str__(self):
        return f"{self.user} likes {self.blog.title}"
    

class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes_user_comment")
    comment = models.ForeignKey(Comments, on_delete=models.CASCADE, related_name="likes_comments")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'comment')  

    def __str__(self):
        return f"{self.user} likes comment by {self.comment.user.first_name}"
    
    