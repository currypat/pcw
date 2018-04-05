# patcurryworks.com/bio/urls.py
from django.urls import path

from bio import views

urlpatterns = [
    path('resume', views.resume, name='resume'),
]
