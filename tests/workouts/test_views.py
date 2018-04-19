# patcurryworks.com/tests/workouts/test_views.py
from .tests import TestWorkoutSetup
from workouts.models import Exercise, Session, Set
from workouts.views import SessionList


workouts_url = '/workouts/'


class TestWorkoutViews(TestWorkoutSetup):

    def test_SessionList_displays_list_of_items(self):
        response = self.client.get(workouts_url + 'sessions/')
        self.assertIn(b'session1', response.content)
        self.assertIn(b'session2', response.content)

    def test_SessionDetail_displays_correct_item(self):
        response = self.client.get(workouts_url + 'sessions/2/')
        self.assertIn(b'session2', response.content)

    def test_SessionDetail_does_not_display_incorrect_item(self):
        response = self.client.get(workouts_url + 'sessions/2/')
        self.assertNotIn(b'session1', response.content)
