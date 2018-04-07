# patcurryworks.com/blog/urls.py
from django.urls import path
from blog import views

app_name='blog'

urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.Index.as_view(), name='index'),
]
