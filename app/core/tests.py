from django.test import TestCase
from django.contrib.auth import get_user_model

from . import models


def sample_user(
        username="Test User",
        email="test@testemail.com",
        password="testpass"
):
    """Create a sample user"""
    return get_user_model().objects.create_user(username, email, password)


def create_post():
    return models.Post.objects.create(
        title="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
        "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        link="https://www.lipsum.com/",
        author_name=sample_user(),
    )


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        username = "Test User"
        email = "test@testemail.com"
        password = "Testpass123"
        user = get_user_model().objects.create_user(
            username=username, email=email, password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_invalid_email(self):
        """Test creating user raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "Test Superuser", "test@testemail.com", "Testpass123"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_post_str(self):
        """Test the post string representation"""
        post = models.Post.objects.create(
            title="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore dolore magna aliqua.",
            link="https://www.lipsum.com/",
            author_name=sample_user(),
        )

        self.assertEqual(str(post), post.title)

    def test_comment_str(self):
        """Test the comment string representation"""
        post = create_post()
        comment = models.Comment.objects.create(
            author_name=post.author_name,
            content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
            "sed do eiusmod tempor incididunt ut labore dolore magna aliqua.",
            post=post,
        )

        self.assertEqual(str(comment), comment.content)
