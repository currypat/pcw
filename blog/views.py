# patcurryworks.com/blog/views.py
from django.shortcuts import render

from blog.models import Post

def index(request):
    post_list = Post.objects.all()
    context = {"post_list": post_list}
    response = render(request, 'blog/index.html', context)
    return response
