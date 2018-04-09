# patcurryworks.com/workouts/views.py
from django.shortcuts import render

def workout_list(request):
    context = {}
    response = render(request, 'workouts/workout_list.html', context)
    return response


#from exercise_api.models import Exercise
#from exercise_api.serializers import ExerciseSerializer
#from rest_framework import generics


#class ExerciseList(generics.ListCreateAPIView):
#    queryset = Exercise.objects.all()
#    serializer_class = ExerciseSerializer


#class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Exercise.objects.all()
#    serializer_class = ExerciseSerializer
