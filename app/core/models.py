from django.contrib.auth.models import User
from django.db import models


class BaseNews(models.Model):
    creation_date = models.DateField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Post(BaseNews):

    title = models.CharField(max_length=255)
    link = models.URLField()
    upvotes = models.ManyToManyField(User,
                                     blank=True,
                                     related_name='vote_users')

    def __str__(self):
        return self.title


class Comment(BaseNews):

    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE,
                             related_name="comments")
    content = models.CharField(max_length=5000)

    def __str__(self):
        return self.content
