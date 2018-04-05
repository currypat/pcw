# patcurryworks.com/tests/bio/tests.py
from django.test import TestCase
from django.urls import resolve

from bio.views import resume, index

class ResumeViewTests(TestCase):

    def setUp(self):
        self.resume_url = '/bio/resume'

    def test_resume_view_resolves_to_resume_view(self):
        found = resolve(self.resume_url)
        self.assertEqual(found.func, resume)

    def test_resume_view_returns_200_status_code(self):
        response = self.client.get(self.resume_url)
        self.assertEqual(response.status_code, 200)

    def test_resume_view_has_Resume_in_it(self):
        response = self.client.get(self.resume_url)
        self.assertIn('Resume', response.content.decode('utf-8'))


class BioIndexViewTests(TestCase):

    def setUp(self):
        self.bio_url = '/bio/'

    def test_bio_index_view_resolves_to_bio_index_view(self):
        found = resolve(self.bio_url)
        self.assertEqual(found.func, index)

    def test_bio_index_view_returns_200_status_code(self):
        response = self.client.get(self.bio_url)
        self.assertEqual(response.status_code, 200)

    def test_resume_view_has_Bio_in_it(self):
        response = self.client.get(self.bio_url)
        self.assertIn('Bio', response.content.decode('utf-8'))

