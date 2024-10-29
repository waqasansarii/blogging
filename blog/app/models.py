from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    
    username = None
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['first_name','last_name']
    
    dob = models.DateField()
    
    roles_choices = [
        (0,'reader'),
        (1,'admin'),
        (2,'moderator'),
        (3,'author')
    ]
    roles = models.IntegerField(choices=roles_choices,default=0)
        