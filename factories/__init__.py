import uuid
import factory
from faker import Faker
from factory.django import DjangoModelFactory

from bidding.user.models import User

fake = Faker('pt_BR')


class UserFactory(DjangoModelFactory):
    id = factory.LazyAttribute(lambda x: uuid.uuid4())
    username = factory.LazyAttribute(lambda x: fake.name())
    email = factory.LazyAttribute(lambda x: fake.email())
    first_name = factory.LazyAttribute(lambda x: fake.first_name())
    last_name = factory.LazyAttribute(lambda x: fake.last_name())
    is_active = factory.LazyAttribute(lambda x: True)
    is_email_verified = factory.LazyAttribute(lambda x: False)
    is_superuser = factory.LazyAttribute(lambda x: False)

    class Meta:
        model = User
