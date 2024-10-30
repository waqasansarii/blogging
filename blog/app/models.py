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


class Category(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)        