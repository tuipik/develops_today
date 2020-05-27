from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Post, Comment

from .serializers import PostSerializer

POSTS_URL = reverse("post:post-list")


def detail_url(post_id):
    """Return post detail URL"""
    return reverse("post:post-detail", args=[post_id])


def sample_post(author_name, **params):
    """Create and return a sample post"""
    defaults = {
        "title": "Sample post",
        "link": "http://sample-link.com",
    }
    defaults.update(params)

    return Post.objects.create(author_name=author_name, **defaults)


def sample_comment(author_name, post, **params):
    """Create and return a sample post"""
    defaults = {
        "post": post,
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
        "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    }
    defaults.update(params)

    return Comment.objects.create(author_name=author_name, **defaults)


class PostApiTests(TestCase):
    """Test unauthenticated recipe API access"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            "Test User", "test@testemail.com", "testpass"
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_posts(self):
        """Test retrieving a list of posts"""
        sample_post(author_name=self.user)
        sample_post(author_name=self.user)

        res = self.client.get(POSTS_URL)

        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_view_post_detail(self):
        """Test viewing a post detail"""
        post = sample_post(author_name=self.user)

        url = detail_url(post.id)
        res = self.client.get(url)

        serializer = PostSerializer(post)
        self.assertEqual(res.data, serializer.data)

    def test_comments_in_post_count(self):
        """Test the count of post's comments"""
        num_of_comments = 3
        post = sample_post(author_name=self.user)

        for comment in range(num_of_comments):
            sample_comment(author_name=self.user, post=post)

        url = detail_url(post.id)
        res = self.client.get(url)

        self.assertEqual(res.data["total_comments"], num_of_comments)

    def test_another_user_comment_post_success(self):
        """Test user comment the post created by another user"""
        post = sample_post(author_name=self.user)

        another_user = get_user_model().objects.create_user(
            "Another Test User", "test123@testemail.com", "testpass123"
        )

        sample_comment(author_name=another_user, post=post)

        url = detail_url(post.id)
        res = self.client.get(url)
        serializer = PostSerializer(post)
        self.assertEqual(
            res.data["comments"][0]["author_name"],
            serializer.data["comments"][0]["author_name"],
        )

    def test_delete_post_success(self):
        """Test delete post success"""
        post = sample_post(author_name=self.user)
        url = detail_url(post.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_decline_delete_post_by_another_user(self):
        """Test delete post by another user is declined"""
        another_user = get_user_model().objects.create_user(
            "Another Test User", "test123@testemail.com", "testpass123"
        )
        post = sample_post(author_name=another_user)
        url = detail_url(post.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_304_NOT_MODIFIED)

    def test_update_upvotes(self):
        """Test update upvotes"""
        upvotes = 3
        post = sample_post(author_name=self.user)
        url = detail_url(post.id)
        res = self.client.patch(url, {"upvotes": upvotes})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["upvotes"], upvotes)

    def test_update_upvotes_by_another_user(self):
        """Test update upvotes by another user"""
        upvotes = 3
        another_user = get_user_model().objects.create_user(
            "Another Test User", "test123@testemail.com", "testpass123"
        )

        post = sample_post(author_name=another_user)
        url = detail_url(post.id)
        res = self.client.patch(url, {"upvotes": upvotes})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["upvotes"], upvotes)
