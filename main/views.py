# patcurryworks.com/main/views.py
from django.http import HttpResponse

def home(request):
    context = {}
    response = render(request, 'main/home.html', context)
    return response
