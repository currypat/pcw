# patcurryworks.com/workouts/models.py
from django.db import models
from django.utils.text import slugify
import datetime

"""
There needs to be a many to many relationship between exercise and set.


https://www.medicinenet.com/weight_lifting/article.htm#how_do_i_go_about_lifting_for_tone_and_endurance
Sets and reps are the terms used to describe the number of times you perform an exercise. A rep is the number of times you perform a specific exercise, and a set is the number of cycles of reps that you complete. For example, suppose you complete 15 reps of a bench press. You would say you've completed "one set of 15 reps." A set can be any number of reps, so if you complete 10 reps of a bench press, you would say you've completed "one set of 10 reps," and if you complete just five reps, then that would be "one set of five reps."
"""


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

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.exercise_slug = slugify(self.title + d)
        super(Exercise, self).save(*args, **kwargs)


class Session(models.Model):
    """This session can have many sets of different types."""
    pub_date= models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True)
    session_slug = models.SlugField(max_length=100, blank=True, null=True)
    exercises = models.ManyToManyField(
        Exercise,
        through='Set',
        through_fields=('session', 'exercise'),
        #related_name='sessions',
    )

    def save(self, *args, **kwargs):
        d = datetime.datetime.today().strftime('%Y-%m-%d')
        self.session_slug = slugify(self.title + '-' + d)
        super(Session, self).save(*args, **kwargs)

class Set(models.Model):
    """This set can have many repetitions of one exercise.
    Sit is going to be a through field for the relationship between
    the Exercise and Session models."""
    session = models.ForeignKey(Session, on_delete=models.CASCADE, blank=True, null=True)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.IntegerField(default=1, blank=True, null=True)
    units = models.CharField(
        max_length=4,
        choices=UNIT_CHOICES,
        default=REPETITIONS
    )

