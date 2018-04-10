from django.conf.urls import url
from workouts import views

app_name='workouts'

urlpatterns = [
    url(r'^$', views.SessionList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.SessionDetail.as_view()),
]
