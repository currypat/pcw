#from django.conf.urls import url
#from exercise_api import views

#urlpatterns = [
#    url(r'^exercises/$', views.exercise_list),
#    url(r'^exercises/(?P<pk>[0-9]+)/$', views.exercise_detail),
#]

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from exercise_api import views

urlpatterns = [
    url(r'^exercises/$', views.ExerciseList.as_view()),
    url(r'^exercises/(?P<pk>[0-9]+)/$', views.ExerciseDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
