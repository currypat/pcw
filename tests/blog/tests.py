# patcurryworks.com/tests/blog/tests.py
from django.test import TestCase
from django.urls import resolve

from blog.views import index

class BlogViewTests(TestCase):

    def setUp(self):
        self.blog_url = '/blog/'

    def test_blog_index_resolves_to_blog_index_view(self):
        found = resolve(self.blog_url)
        self.assertEqual(found.func, index)

    def test_blog_index_returns_200_status_code(self):
        response = self.client.get(self.blog_url)
        self.assertEqual(response.status_code, 200)

    def test_blog_index_view_has_Blog_in_it(self):
        response = self.client.get(self.blog_url)
        self.assertIn('Blog', response.content.decode('utf-8'))




