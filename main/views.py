# patcurryworks.com/main/views.py
from django.shortcuts import render

def home(request):
    context = {}
    response = render(request, 'main/home.html', context)
    return response
