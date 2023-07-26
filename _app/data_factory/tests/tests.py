from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status


class TestTokenPostTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            "ousmane", "ous@ous.com", "ousmane209"
        )
        self.token = Token.objects.create(user=self.user)

    def test_login(self):
        self.client.login(username="ousmane", password="ousmane209")
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        response = self.client.post(
            "/api/Translations/",
            {"query": "bonjour", "user": self.user.id, "to": "it"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
