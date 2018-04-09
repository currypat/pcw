# patcurryworks.com/blog/views.py
from django.core import serializers
from django.views import View
from django.shortcuts import render, get_object_or_404

from blog.models import Post

def post_list(request):
    post_list = Post.objects.all()
    context = {'post_list': post_list}
    response = render(request, 'blog/post_list.html', context)
    return response

def post_detail(request, post_slug):
    post = get_object_or_404(Post, post_slug=post_slug)
    context = {'post': post}
    response = render(request, 'blog/post_detail.html', context)
    return response
