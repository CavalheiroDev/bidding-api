import pytest
from faker import Faker

from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from bidding.user.models import User


class TestUserAuthAPIView:

    def setup(self):
        self.fake = Faker()
        self.url = reverse('user-refresh-auth')
        self.api_client = APIClient()

    @pytest.mark.django_db
    def test_should_return_invalid_refresh(self, authentication_refresh_user_invalid_credentials):
        data = {
            'refresh': self.fake.pystr()
        }

        response = self.api_client.post(self.url, data=data)

        assert response.status_code == 401
        assert response.json() == authentication_refresh_user_invalid_credentials

    @pytest.mark.django_db
    def test_should_return_valid_refresh(self):
        password = self.fake.pystr()
        user = User.objects.create_user(username=self.fake.name(), password=password)
        user_data = {
            'username': user.username,
            'password': password
        }

        serializer = TokenObtainPairSerializer(data=user_data)
        serializer.is_valid(raise_exception=True)

        refresh = serializer.validated_data['refresh']
        data = {
            'refresh': refresh
        }

        response = self.api_client.post(self.url, data=data)

        assert response.status_code == 200
        assert 'access' in response.json()
