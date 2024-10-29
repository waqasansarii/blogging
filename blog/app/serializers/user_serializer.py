from rest_framework import serializers
from ..models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    class Meta:
        model = User
        fields=['first_name','last_name','roles','dob','email','password']
        # fields='__all__'
 

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password= serializers.CharField(write_only=True)
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        # fields='__all__' 
        fields=['first_name','last_name','roles','dob','email','is_superuser','is_active']
           