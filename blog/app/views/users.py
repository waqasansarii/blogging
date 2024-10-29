from rest_framework.viewsets import ModelViewSet
from ..models import User
from ..serializers.user_serializer import UserSerializer


class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer