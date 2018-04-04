# patcurryworks.com/blog/views.py
from django.shortcuts import render

def index(request):
    context = {}
    response = render(request, 'blog/index.html', context)
    return response
