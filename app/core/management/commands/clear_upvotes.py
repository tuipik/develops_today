from django.core.management.base import BaseCommand

from core.models import Post


class Command(BaseCommand):
    help = 'Clear upvotes'

    def clear_post_upvotes(self):
        posts = Post.objects.all()
        for post in posts:
            post.upvotes.clear()

    def handle(self, *args, **options):
        self.clear_post_upvotes()
