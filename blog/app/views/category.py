from rest_framework.viewsets import ModelViewSet

from ..serializers.category_serializer import CategorySerializer
from ..models import Category



class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer