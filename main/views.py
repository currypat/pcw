# patcurryworks.com/main/views.py
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    response = render(request, 'main/home.html', {})
    return response
