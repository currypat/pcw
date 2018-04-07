# patcurryworks.com/blog/views.py
from django.core import serializers
from django.views import View
from django.shortcuts import render

from blog.models import Post

def index(request):
    post_list = Post.objects.all()

    post_list_serialized = serializers.serialize('json',
                                                 post_list,
                                                 fields=("text")) 

    props = {
        'users': [
            {'username': 'alice'},
            {'username': 'bob'},
        ]
    }


    context = {
        'post_list': post_list,
        'post_list_serialized': post_list_serialized,
        'props':props
    }
    response = render(request, 'blog/index.html', context)
    return response
