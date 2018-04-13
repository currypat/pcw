# patcurryworks.com/workouts/views.py
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from workouts.models import Exercise, Set, Session

class SessionList(ListView):
    model = Session

class SessionDetail(DetailView):
    model = Session

class SessionCreate(CreateView):
    model = Session
    fields = ('title',)

class SessionUpdate(UpdateView):
    model = Session

class SessionDelete(DeleteView):
    model = Session


#class ExerciseList(generics.ListCreateAPIView):
#    queryset = Exercise.objects.all()
#    serializer_class = ExerciseSerializer
#
#
#class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Exercise.objects.all()
#    serializer_class = ExerciseSerializer
#
#
#class SetList(generics.ListCreateAPIView):
#    queryset = Set.objects.all()
#    serializer_class = SetSerializer
#
#
#class SetDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Set.objects.all()
#    serializer_class = SetSerializer
#   
#
#class SessionList(generics.ListCreateAPIView):
#    queryset = Session.objects.all()
#    serializer_class = SessionSerializer
#
#
#class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
#    queryset = Session.objects.all()
#    serializer_class = SessionSerializer
   
