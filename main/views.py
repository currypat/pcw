# patcurryworks.com/main/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse('Pat Curry Works')
