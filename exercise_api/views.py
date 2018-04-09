# patcurryworks.com/exercise_api/views.py
from exercise_api.models import Exercise
from exercise_api.serializers import ExerciseSerializer
from rest_framework import generics


class ExerciseList(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
