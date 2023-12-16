from django.contrib.auth.models import User
from django.test import TestCase

from django.test import TestCase
from myapp.models import Animal


class LoginTestCase(TestCase):
    def setUp(self):
        Juegos.objects.create(name="Agustin",)


    def test_juegos_return(self):
        """Animals that can speak are correctly identified"""
        user = User.objects.get(name="Agustin")

        self.assertEqual(Juegos.user.username(), 'Agustin')
