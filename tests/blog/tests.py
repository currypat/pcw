# patcurryworks.com/tests/blog/tests.py
from django.test import TestCase
from django.urls import resolve

from blog.views import index

class ViewTests(TestCase):

    def test_blog_index_resolves_to_home_page_view(self):
        #response = self.client.get("/blog/")
        #self.assertEqual(response.status_code, 200)
        found = resolve('/blog/')
        self.assertEqual(found.func, index)


