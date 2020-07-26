from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def setUp(self):
        self.email = 'test@tekpoetics.com'
        self.name = 'test name'
        self.password = "testingpass12"

    def test_create_user_with_email(self):
        # test for creating a new user using email instead of username

        user = get_user_model().objects.create_user(
            email=self.email,
            name=self.name,
            password=self.password
        )

        self.assertEqual(user.email, self.email)
        self.assertTrue(user.check_password(self.password))

    def test_email_ormalizes(self):
        '''test the email address for new user is normalized!'''
        user = get_user_model().objects.create_user(
            email="test@TekpoetICS.COM",
            name=self.name,
            password=self.password
        )

        self.assertEqual(user.email, self.email)
