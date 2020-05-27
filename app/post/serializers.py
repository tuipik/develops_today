from rest_framework import serializers, permissions

from core.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for comment objects"""

    author_name = serializers.ReadOnlyField(source="author_name.username")

    class Meta:
        model = Comment
        fields = ("id", "post", "author_name", "content", "creation_date")
        read_only_fields = ("id",)


class PostSerializer(serializers.ModelSerializer):
    """Serializer for post objects"""

    comments = CommentSerializer(many=True, read_only=True)
    total_comments = serializers.SerializerMethodField(read_only=True)
    author_name = serializers.ReadOnlyField(source="author_name.username")
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "link",
            "creation_date",
            "upvotes",
            "author_name",
            "total_comments",
            "comments",
        )
        read_only_fields = ("id",)

    def get_total_comments(self, obj):
        return obj.comments.count()
