from abc import abstractmethod
from typing import Optional

from bidding.user.models import User
from bidding.user.exceptions import UserNotFound
from bidding.user.types import UserCreatorTypedDict

from utils.contracts_repositories import Repositories


class IUserRepository(Repositories):
    model = User
    not_found_exception = UserNotFound

    @abstractmethod
    def create_user(self, *, data: UserCreatorTypedDict) -> User:
        raise NotImplementedError()

    @abstractmethod
    def find_or_raise_by_email(self, *, email: str) -> Optional[User]:
        raise NotImplementedError()

    @abstractmethod
    def find_or_raise_by_username(self, *, username: str) -> Optional[User]:
        raise NotImplementedError()
