# patcurryworks.com/bio/urls.py
from django.urls import path
from bio import views

app_name = 'bio'


urlpatterns = [
    path('', views.index, name='index'),
    path('resume', views.resume, name='resume'),
]
