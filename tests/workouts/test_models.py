# patcurryworks.com/tests/workouts/test_models.py
from .tests import TestWorkoutSetup
from workouts.models import Exercise, Session, Set
        
class TestWorkoutModels(TestWorkoutSetup):

    def test_that_list_of_exercises_can_be_brought_back(self):
        """This test is pointless"""
        exercise_list = Exercise.objects.all()
        self.assertNotEqual(exercise_list[0].title, exercise_list[1].title)

    def test_that_list_of_sessions_can_be_brought_back(self):
        """This test is pointless"""
        session_list = Session.objects.all()
        self.assertNotEqual(session_list[0].title, session_list[1].title)

    def test_that_sets_can_be_brought_back_from_sessions(self):
        self.assertEqual(self.session1set1.exercise, self.pushup)
        self.assertEqual(self.session2set1.amount, 2)

    # test sets can be deleted

    # test sets can be updated

    # test sets can be updated
