from django.urls import path, re_path
from workouts import views
from workouts import api_views

app_name='workouts'

urlpatterns = [

    ############################
    # normal django view urls
    ############################

    path('', views.SessionList.as_view(), name='SessionList'),
    re_path(r'^(?P<pk>[0-9]+)/$', views.SessionDetail.as_view(), name='SessionDetail'),

    ############################
    # django rest framework urls
    ############################

    # sessions
    path('api/sessions/', api_views.SessionList.as_view(), name='SessionListAPI'),
    re_path(r'^api/sessions/(?P<pk>[0-9]+)/$', api_views.SessionDetail.as_view(), name='SessionDetailAPI'),

    #sets
    path('api/sets/', api_views.SetList.as_view(), name='SetListAPI'),
    re_path(r'^api/sets/(?P<pk>[0-9]+)/$', api_views.SetDetail.as_view(), name='SetDetailAPI'),

    # exercises
    path('api/exercises/', api_views.ExerciseList.as_view(), name='ExerciseListAPI'),
    re_path(r'^api/exercises/(?P<pk>[0-9]+)/$', api_views.ExerciseDetail.as_view(), name='ExerciseDetailAPI'),

    ############################
    # graphql urls ?
    ############################

]
