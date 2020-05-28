from rest_framework import serializers, permissions
from django.contrib.auth import get_user_model
from core.models import Post, Comment


UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user

    class Meta:
        model = UserModel
        fields = ('password', 'username', 'first_name', 'last_name',)


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
