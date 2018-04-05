# patcurryworks.com/bio/views.py
from django.shortcuts import render

def resume(request):
    context = {}
    response = render(request, 'bio/resume.html', context)
    return response
    
