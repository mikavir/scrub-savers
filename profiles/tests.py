import os
if os.path.exists("env.py"):
    import env  # noqa
from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User


password = os.environ.get("TEST_PASSWORD")
email = os.environ.get("TEST_EMAIL")


class TestViews(TestCase):

    def test_profile_page(self):
        """ Test views on profile page """
        # Log user in
        self.client = Client()
        user = User.objects.create_user('test_admin', password)
        self.client.force_login(user=user)
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
