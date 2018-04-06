# patcurryworks.com/blog/views.py
from django.views import View
from django.shortcuts import render

from blog.models import Post

def index(request):
    post_list = Post.objects.all()

    props = {
        'users': [
            {'username': 'alice'},
            {'username': 'bob'},
        ]
    }


    context = {
        'post_list': post_list,
        'props':props
    }
    response = render(request, 'blog/index.html', context)
    return response

#class Index(View):
#    def get(self, request):
#        props = {
#            'users': [
#                {'username': 'alice'},
#                {'username': 'bob'},
#            ]
#        }
#
#        post_list = Post.objects.all()
#
#        context = {
#            'props': props,
#            'post_list': post_list
#        }
#
#        render(request, 'blog/index.html', context)
