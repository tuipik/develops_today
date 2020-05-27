from core.models import Post, Comment

from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from .mixins import NewsViewSetMixin


class PostViewSet(NewsViewSetMixin):
    serializer_class = serializers.PostSerializer
    queryset = Post.objects.all()


class UpvoteView(APIView):
    def put(self, request, pk, format=None):
        post = Post.objects.filter(id=pk).first()
        post.upvotes.add(self.request.user)
        return Response(200)


class CommentViewSet(NewsViewSetMixin):
    serializer_class = serializers.CommentSerializer
    queryset = Comment.objects.all()
