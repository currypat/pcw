# patcurryworks.com/test/blog/test_models.py
from django.test import TestCase

from blog.models import Post


class PostModelTests(TestCase):

    def test_that_post_can_be_created(self):
        Post.objects.create(text='first post')
        self.assertEqual(len(Post.objects.all()), 1)
