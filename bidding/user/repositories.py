from typing import Optional

from bidding.user.models import User
from bidding.user.contracts import IUserRepository
from bidding.user.types import UserCreatorTypedDict
from bidding.user.exceptions import UserAlreadyExists


class PostgresUserRepository(IUserRepository):

    def create_user(self, *, data: UserCreatorTypedDict) -> User:
        password = data.pop('password')
        user = self.model(**data)
        user.set_password(password)
        user.save()
        return user

    def find_or_raise_by_email(self, *, email: str) -> Optional[User]:
        user = self.safe_get(email=email)
        if user:
            raise UserAlreadyExists('User with this email already exists')
        return user

    def find_or_raise_by_username(self, *, username: str) -> Optional[User]:
        user = self.safe_get(username=username)
        if user:
            raise UserAlreadyExists('User with this username already exists')
        return user
