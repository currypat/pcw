# patcurryworks.com/blog/urls.py
from django.urls import path, re_path
from blog import views

app_name='blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    re_path('^(?P<post_slug>[-\w]*)/$', views.post_detail, name='post_detail'),
    #path('', views.Index.as_view(), name='index'),
]
