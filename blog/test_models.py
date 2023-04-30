from django.test import TestCase
from .models import Post, Comment

class TestDjango(TestCase):
    def test_this_thing_works(self):
        self.assertEqual(1, 0)