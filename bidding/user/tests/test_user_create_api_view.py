import pytest
from faker import Faker

from django.urls import reverse
from rest_framework.test import APIClient

from factories import UserFactory


class TestUserCreateApiView:

    def setup(self):
        self.fake = Faker('pt_BR')
        self.url = reverse('user-create')
        self.api_client = APIClient()

    @pytest.mark.django_db
    def test_should_return_successful(self):
        data = {
            'username': self.fake.name(),
            'password': self.fake.pystr(),
            'email': self.fake.email(),
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'is_superuser': False
        }

        response = self.api_client.post(self.url, data=data)

        response_data = response.json()

        assert response.status_code == 201
        assert response_data.get('username') == data.get('username')
        assert response_data.get('email') == data.get('email')
        assert response_data.get('first_name') == data.get('first_name')
        assert response_data.get('last_name') == data.get('last_name')
        assert response_data.get('is_superuser') == data.get('is_superuser')

    @pytest.mark.django_db
    def test_should_return_username_already_exists(self, error_message_create_user_with_username_already_exists):
        username = self.fake.name()
        UserFactory.create(username=username)

        data = {
            'username': username,
            'password': self.fake.pystr(),
            'email': self.fake.email(),
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'is_superuser': False
        }

        response = self.api_client.post(self.url, data=data)

        assert response.status_code == 400
        assert response.json() == error_message_create_user_with_username_already_exists

    @pytest.mark.django_db
    def test_should_return_email_already_exists(self, error_message_create_user_with_email_already_exists):
        email = self.fake.email()
        UserFactory.create(email=email)

        data = {
            'username': self.fake.name(),
            'password': self.fake.pystr(),
            'email': email,
            'first_name': self.fake.first_name(),
            'last_name': self.fake.last_name(),
            'is_superuser': False
        }

        response = self.api_client.post(self.url, data=data)

        assert response.status_code == 400
        assert response.json() == error_message_create_user_with_email_already_exists

    def test_should_return_body_empty(self, error_message_create_user_with_empty_body):
        response = self.api_client.post(self.url, data={})

        assert response.status_code == 400
        assert response.json() == error_message_create_user_with_empty_body
