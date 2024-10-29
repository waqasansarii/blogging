from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate,login,logout

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from ..models import User
from ..serializers.user_serializer import RegisterSerializer,LoginSerializer


# class UserView(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer
 
@permission_classes([AllowAny])    
class RegisterView(APIView):
    def post(self,request:Request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        # user_model = User
        if serializer.is_valid():
            serializer.validated_data['password'] = make_password(serializer.validated_data['password'])
            serializer.save()
            return Response({"user":serializer.data,"msg":'user created successfully'},status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
        
        
@permission_classes([AllowAny])        
class LoginView(APIView):
    def post(self,request:Request):
        data = request.data
        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            password = make_password(serializer.validated_data['password'])
            print(password,'login')
            user = authenticate(request, email=serializer.validated_data['email'],password=serializer.validated_data['password'])
            if user is not None:
                login(request,user=user)
                return Response('Login successfully',status.HTTP_200_OK)
            else:
                return Response('invalid credentials',status.HTTP_200_OK)
        else:
            print('invalid result')
            return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)            


class LogoutView(APIView):
    def post(self,req:Request):
        logout(req)
        return Response('logout success',status.HTTP_200_OK)        