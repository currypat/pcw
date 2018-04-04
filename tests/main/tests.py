# patcurryworks.com/tests/blog/tests.py
from django.test import TestCase
from django.urls import resolve

from main.views import home

class MainViewTests(TestCase):

    def setUp(self):
        self.home_url = '/'

    def test_home_resolves_to_home_view(self):
        """Is this redundant?"""
        found = resolve(self.home_url)
        self.assertEqual(found.func, home)

    def test_home_resolves_to_home_view(self):
        """Is this redundant?"""
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)

    def test_home_view_has_pat_curry_works_in_it(self):
        response = self.client.get(self.home_url)
        self.assertIn('Pat Curry Works', response.content.decode("utf-8"))


