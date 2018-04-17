from django.urls import path, re_path
from django.views.generic import TemplateView
from workouts import views
from workouts import api_views

app_name='workouts'

urlpatterns = [

    ############################
    # normal django view urls
    ############################
    # workouts index view
    path('', TemplateView.as_view(template_name='workouts/workout_index.html'), name='WorkoutIndex'),

    # sessions
    path('sessions/', views.SessionList.as_view(), name='SessionList'),
    path('sessions/new/', views.SessionCreate.as_view(), name='SessionCreate'),
    re_path(r'^sessions/(?P<pk>[0-9]+)/$', views.SessionDetail.as_view(), name='SessionDetail'),
    re_path(r'^sessions/(?P<pk>[0-9]+)/update/$', views.SessionUpdate.as_view(), name='SessionUpdate'),
    re_path(r'^sessions/(?P<pk>[0-9]+)/delete/$', views.SessionDelete.as_view(), name='SessionDelete'),

    # exercises
    path('exercises/', views.ExerciseList.as_view(), name='ExerciseList'),
    path('exercises/new/', views.ExerciseCreate.as_view(), name='ExerciseCreate'),
    re_path(r'^exercises/(?P<slug>[-\w]*)/$', views.ExerciseDetail.as_view(), name='ExerciseDetail'),
    re_path(r'^exercises/(?P<slug>[-\w]*)/update/$', views.ExerciseUpdate.as_view(), name='ExerciseUpdate'),
    re_path(r'^exercises/(?P<slug>[-\w]*)/delete/$', views.ExerciseDelete.as_view(), name='ExerciseDelete'),

    # sessions - sets

    # exercises - sets

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
