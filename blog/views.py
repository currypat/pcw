# patcurryworks.com/blog/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse('Blog')
