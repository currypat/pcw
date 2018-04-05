# patcurryworks.com/bio/views.py
from django.shortcuts import render


def index(request):
    context = {}
    response = render(request, 'bio/index.html', context)
    return response
 
def resume(request):
    context = {}
    response = render(request, 'bio/resume.html', context)
    return response
   
