from core.models import Post, Comment
from . import serializers
from .mixins import NewsViewSetMixin


class PostViewSet(NewsViewSetMixin):
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()


class CommentViewSet(NewsViewSetMixin):
    serializer_class = serializers.CommentSerializer
    queryset = Comment.objects.all()
