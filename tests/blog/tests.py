# patcurryworks.com/tests/blog/tests.py
from django.test import TestCase
from django.urls import resolve

from blog.views import post_list, post_detail
from blog.models import Post

class PostListViewTests(TestCase):

    def setUp(self):
        self.blog_url = '/blog/'
        self.post1 = Post.objects.create(title='post one', text='first post')
        self.post2 = Post.objects.create(title='post two', text='second post')

    def test_post_list_resolves_to_post_list_view(self):
        found = resolve(self.blog_url)
        self.assertEqual(found.func, post_list)

    def test_post_list_returns_200_status_code(self):
        response = self.client.get(self.blog_url)
        self.assertEqual(response.status_code, 200)

    def test_post_list_view_has_Blog_in_it(self):
        response = self.client.get(self.blog_url)
        self.assertIn('Blog', response.content.decode('utf-8'))

    def test_post_list_view_returns_list_of_blog_posts(self):
        response = self.client.get(self.blog_url)
        self.assertIn('post one', response.content.decode('utf-8'))
        self.assertIn('post two', response.content.decode('utf-8'))


class PostDetailViewTests(TestCase):
    
    def setUp(self):
        self.blog_url = '/blog/'
        self.post1 = Post.objects.create(title='post one', text='first post')

    def test_post_detail_resolves_to_post_detail_view(self):
        found = resolve(self.blog_url + 'post-one/')
        self.assertEqual(found.func, post_detail)

    def test_post_detail_returns_200_status_code(self):
        response = self.client.get(self.blog_url + 'post-one/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_has_post_title_in_content(self):
        response = self.client.get(self.blog_url + 'post-one/')
        self.assertIn('post one', response.content.decode('utf-8'))

    def test_post_detail_has_post_text_in_content(self):
        response = self.client.get(self.blog_url + 'post-one/')
        self.assertIn('first post', response.content.decode('utf-8'))
