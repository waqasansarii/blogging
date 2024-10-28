from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # class Meta:
    username = None
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS=['first_name','last_name']
    dob = models.DateField()
        