# patcurryworks.com/blog/views.py
from django.shortcuts import render

def index(request):
    response = render(request, 'blog/index.html', {})
    return response
