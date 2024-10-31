from rest_framework.viewsets import ModelViewSet
from ..serializers.comment_serializer import CommentSerializer
from ..models import Comments


class CommentView(ModelViewSet):
    queryset = Comments.objects.select_related('user').all()
    serializer_class = CommentSerializer