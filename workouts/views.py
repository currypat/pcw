# patcurryworks.com/workouts/views.py
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic import CreateView, UpdateView, DeleteView
from workouts.models import Exercise, Set, Session


# Session views
class SessionList(ListView):
    model = Session

    
class SessionDetail(DetailView):
    """The sets will be creatable from this page."""
    model = Session

    
class SessionCreate(CreateView):
    model = Session
    fields = ['title']
    template_name = 'workouts/session_create.html'

    def get_success_url(self):
        return reverse('workouts:SessionDetail', kwargs={'pk': self.object.pk})

    
class SessionUpdate(UpdateView):
    model = Session
    fields = ['title']
    success_url = reverse_lazy('workouts:SessionList')

    
class SessionDelete(DeleteView):
    model = Session
    success_url = reverse_lazy('workouts:SessionList')


# Exercise views
class ExerciseList(ListView):
    model = Exercise


class ExerciseDetail(DetailView):
    model = Exercise
    slug_field = 'exercise_slug'

# Set views



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
   
