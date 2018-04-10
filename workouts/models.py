# patcurryworks.com/workouts/models.py
from django.db import models
from django.utils.text import slugify

"""
https://www.medicinenet.com/weight_lifting/article.htm#how_do_i_go_about_lifting_for_tone_and_endurance
Sets and reps are the terms used to describe the number of times you perform an exercise. A rep is the number of times you perform a specific exercise, and a set is the number of cycles of reps that you complete. For example, suppose you complete 15 reps of a bench press. You would say you've completed "one set of 15 reps." A set can be any number of reps, so if you complete 10 reps of a bench press, you would say you've completed "one set of 10 reps," and if you complete just five reps, then that would be "one set of five reps."
"""


# Session
# Set
# Rep
# Exercise

SECONDS = 'sec'
REPETITIONS = 'reps'
UNIT_CHOICES = (
    (SECONDS, 'seconds'),
    (REPETITIONS, 'repetitions'),
)


class Exercise(models.Model):
    """This is the smallest individual unit."""
    title = models.CharField(max_length=50, blank=True, null=True)
    exercise_slug = models.SlugField(max_length=50, blank=True, null=True)



    def save(self, *args, **kwargs):
        self.exercise_slug = slugify(self.title)
        super(Exercise, self).save(*args, **kwargs)

class Set(models.Model):
    """This set can have many repetitions of one exercise."""
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1, blank=True, null=True)
    units = models.CharField(
        max_length=4,
        choices=UNIT_CHOICES,
        default=REPETITIONS
    )

class Session(models.Model):
    """This session can have many sets of different types."""
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    sets = models.ForeignKey(Set, on_delete=models.CASCADE)



#    amount = models.IntegerField(default=1)
#    sets = models.IntegerField(default=1)
#    units = models.CharField(
#        max_length=4,
#        choices=UNIT_CHOICES,
#        default=REPETITIONS
#    )

#    class Meta:
#        ordering = ('created',)
        

#class Set(models.Model):
#    """This set can have many exercises."""

#class Exercise(models.Model):
#    """This is the number of times a particular exercise was performed during a set.
#    It should probably be called reps or something, and not Exercise. Exercise might
#    be actually the individual exercise.
#    """
    
