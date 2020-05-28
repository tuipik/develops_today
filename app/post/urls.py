from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, UpvoteView, CreateUserView

router = DefaultRouter()
router.register("post", PostViewSet, basename="post")
router.register("comment", CommentViewSet, basename="comment")
router.register("createuser", CreateUserView)

app_name = "post"

urlpatterns = [
    path("post/<int:pk>/upvote/", UpvoteView.as_view(), name='upvotes'),
    path("", include(router.urls)),
]
