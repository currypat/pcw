# patcurryworks.com/tests/blog/tests.py
from django.test import TestCase
from django.urls import resolve

from blog.views import index
from blog.models import Post

class BlogIndexViewTests(TestCase):

    def setUp(self):
        self.blog_url = '/blog/'
        self.post1 = Post.objects.create(text='first post')
        self.post2 = Post.objects.create(text='second post')
        self.post3 = Post.objects.create(text='third post')



    def test_blog_index_resolves_to_blog_index_view(self):
        found = resolve(self.blog_url)
        self.assertEqual(found.func, index)

    def test_blog_index_returns_200_status_code(self):
        response = self.client.get(self.blog_url)
        self.assertEqual(response.status_code, 200)

    def test_blog_index_view_has_Blog_in_it(self):
        response = self.client.get(self.blog_url)
        self.assertIn('Blog', response.content.decode('utf-8'))

    def test_blog_index_view_returns_list_of_blog_posts(self):
        response = self.client.get(self.blog_url)
        self.assertIn('first post', response.content.decode('utf-8'))
        self.assertIn('second post', response.content.decode('utf-8'))
        self.assertIn('third post', response.content.decode('utf-8'))
