from django.test import TestCase

# Create your tests here.
class FirstTestCase(TestCase):
    def test_one_is_one(self):
        self.assertEqual(1, 1)