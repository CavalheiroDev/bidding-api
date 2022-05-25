import pytest
from faker import Faker

from django.urls import reverse
from rest_framework.test import APIClient

from bidding.user.models import User


class TestUserAuthAPIView:

    def setup(self):
        self.fake = Faker()
        self.url = reverse('user-auth')
        self.api_client = APIClient()

    @pytest.mark.django_db
    def test_should_return_invalid_credentials(self, authentication_user_invalid_credentials):
        data = {
            'username': self.fake.pystr(),
            'password': self.fake.pystr()
        }

        response = self.api_client.post(self.url, data=data)

        assert response.status_code == 401
        assert response.json() == authentication_user_invalid_credentials

    @pytest.mark.django_db
    def test_should_return_valid_credentials(self):
        password = self.fake.pystr()
        user = User.objects.create_user(username=self.fake.name(), password=password)
        data = {
            'username': user.username,
            'password': password
        }

        response = self.api_client.post(self.url, data=data)

        assert response.status_code == 200
        assert 'access' in response.json()
        assert 'refresh' in response.json()
