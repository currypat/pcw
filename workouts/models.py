# patcurryworks.com/workouts/models.py
from django.db import models


SECONDS = 'sec'
REPETITIONS = 'reps'
UNIT_CHOICES = (
    (SECONDS, 'seconds'),
    (REPETITIONS, 'repetitions'),
)


class Workout(models.Model):
    """Workouts"""
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True)
    amount = models.IntegerField(default=1)
    sets = models.IntegerField(default=1)
    units = models.CharField(
        max_length=4,
        choices=UNIT_CHOICES,
        default=REPETITIONS
    )

    class Meta:
        ordering = ('created',)
        


