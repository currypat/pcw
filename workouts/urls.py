from django.urls import path, re_path
from workouts import views
from workouts import api_views

app_name='workouts'

urlpatterns = [
    path('', views.SessionList.as_view(), name='SessionList'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.SessionDetail.as_view(), name='SessionDetail'),

    ####
    # Django Rest Framework 
    path('api/', api_views.SessionList.as_view(), name='SessionListAPI'),
    re_path(r'^api/(?P<pk>[0-9]+)/$', api_views.SessionDetail.as_view(), name='SessionDetailAPI'),
]
