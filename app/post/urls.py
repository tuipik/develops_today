from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, CommentViewSet, UpvoteView

router = DefaultRouter()
router.register("post", PostViewSet, basename="post")
router.register("comment", CommentViewSet, basename="comment")

app_name = "post"

urlpatterns = [
    path("post/<int:pk>/upvote/", UpvoteView.as_view(), name='upvotes'),
    path("", include(router.urls)),
]
