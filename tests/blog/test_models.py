# patcurryworks.com/test/blog/test_models.py
from django.test import TestCase

from blog.models import Post


class PostModelTests(TestCase):

    def setUp(self):
        self.post1 = Post.objects.create(text='first post')
        self.post2 = Post.objects.create(text='second post')
        self.post3 = Post.objects.create(text='third post')

#    def test_that_post_can_be_created(self):
#        Post.objects.create(text='first post')
#        self.assertEqual(len(Post.objects.all()), 1)

    def test_that_list_of_posts_can_be_brought_back(self):
        post_list = Post.objects.all()
        self.assertNotEqual(post_list[0].text, post_list[1].text)
