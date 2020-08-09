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

    def test_email_normalizes(self):
        '''test the email address for new user is normalized!'''
        user = get_user_model().objects.create_user(
            email="test@TekpoetICS.COM",
            name=self.name,
            password=self.password
        )

        self.assertEqual(user.email, self.email)

    def test_empty_email_field(self):

        ''' test if valueError is raised when the email field is empty'''

        self.email = ""

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=self.email,
                name=self.name,
                password=self.password
                )

    def test_create_superuser(self):

        user1 = get_user_model().objects.create_superuser(
            email=self.email,
            name=self.name,
            password=self.password
        )

        '''create superuser without providing name!'''
        user2 = get_user_model().objects.create_superuser(
            email='testuser2@tekpoetics.com',
            password=self.password
        )

        self.assertTrue(user1.is_admin)
        self.assertEqual(user2.name, 'testuser2')
