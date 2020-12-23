from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.
class TestUsers(TestCase):
    user1 = {"first_name": "Michael", "last_name": "Okolo", "email": "okolomikel2009@gmail.com", "username": "mokolo", "password": "pass12345"}
    user2 = {"first_name": "Ginika", "last_name": "Ani", "email": "aniginika@gmail.com", "username": "gani", "password": "pass12345"}

    def testCreateUsers(self):
        self.assertTrue(User.objects.create(**self.user1))
        # self.assertIntegrityError (User.objects.create(**self.user1))
        self.assertTrue(User.objects.create(**self.user2))