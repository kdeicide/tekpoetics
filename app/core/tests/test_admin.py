from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.a_user = get_user_model().objects.create_superuser(
            email="admin.test@tekpoetiks.com",
            password="testingpass123"
        )
        self.client.force_login(self.a_user)
        self.user = get_user_model().objects.create_user(
            email="test@tekpoetics.com",
            name="test user",
            password="test123"
        )

    def test_users_listed(self):

        '''test if users are listed in admin page'''

        url = reverse('admin:core_myuser_changelist')
        result = self.client.get(url)

        self.assertContains(result, self.user.name)
        self.assertContains(result, self.user.email)

    def test_user_change_page(self):
        ''' test if the user edit page works properly'''
        url = reverse("admin:core_myuser_change", args=[self.user.id])
        result = self.client.get(url)

        self.assertEqual(result.status_code, 200)

    def test_admin_add_user(self):
        '''test that the create user page works'''
        url = reverse("admin:core_myuser_add")
        result = self.client.get(url)

        self.assertEqual(result.status_code, 200)
