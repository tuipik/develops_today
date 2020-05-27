from rest_framework import serializers, permissions

from core.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source="author.username")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    class Meta:
        model = Comment
        fields = ("id", "post", "author", "content", "creation_date")
        read_only_fields = ("id",)


class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, read_only=True)
    total_comments = serializers.SerializerMethodField(read_only=True)
    total_upvotes = serializers.SerializerMethodField(read_only=True)
    author = serializers.ReadOnlyField(source="author.username")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "creation_date",
            "total_upvotes",
            "upvotes",
            "author",
            "total_comments",
            "comments",
        )
        read_only_fields = ("id", "upvotes",)

    def get_total_comments(self, obj):
        return obj.comments.count()

    def get_total_upvotes(self, obj):
        return obj.upvotes.count()
