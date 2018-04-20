# patcurryworks.com/tests/workouts/tests.py
from django.test import TestCase
from workouts.models import Exercise, Session, Set

class TestWorkoutSetup(TestCase):

    def setUp(self):
        self.pushup = Exercise.objects.create(title='pushup')
        self.situp = Exercise.objects.create(title='situp')
        self.plank = Exercise.objects.create(title='plank')

        self.session1 = Session.objects.create(title='session1')
        self.session2 = Session.objects.create(title='session2')

        # make sets for session 1
        self.session1set1 = Set.objects.create(
            session=self.session1,
            exercise=self.pushup,
            amount=1,
            units='reps')

        self.session1set2 = Set.objects.create(
            session=self.session1,
            exercise=self.situp,
            amount=1,
            units='reps')

        self.session1set3 = Set.objects.create(
            session=self.session1,
            exercise=self.situp,
            amount=30,
            units='seconds')

        # make sets for session 2
        self.session2set1 = Set.objects.create(session=self.session2,
                                               exercise=self.situp,
                                               amount=2,
                                               units='reps')

        self.session2set2 = Set.objects.create(session=self.session2,
                                               exercise=self.situp,
                                               amount=2,
                                               units='reps')

