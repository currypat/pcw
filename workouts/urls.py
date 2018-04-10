from django.conf.urls import url
from workouts import views

app_name='workouts'

urlpatterns = [
    url(r'^$', views.workout_list),
]
