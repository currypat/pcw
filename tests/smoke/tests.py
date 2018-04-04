# patcurryworks.com/tests/smoke/tests.py
from django.test import TestCase

from main.smoke import sum

class SmokeTests(TestCase):

    def test_sum_adds_two_numbers_correctly(self):
        self.assertEqual(sum(1,2), 3)

