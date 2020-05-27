from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """Post object"""

    title = models.CharField(max_length=255)
    link = models.URLField()
    creation_date = models.DateField(auto_now=True)
    upvotes = models.PositiveIntegerField(blank=True, default=0)
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment object"""

    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="comments"
                             )
    author_name = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=5000)
    creation_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.content
