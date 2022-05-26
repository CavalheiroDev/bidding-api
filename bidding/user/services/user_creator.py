from bidding.user.types import UserCreatorTypedDict
from bidding.user.contracts import IUserRepository


class UserCreator:

    def __init__(self, user_repository: IUserRepository) -> None:
        self._user_repository = user_repository

    def create_user(self, data: UserCreatorTypedDict):
        self.__validate(data)

        user = self._user_repository.create_user(data=data)
        return user

    def __validate(self, data: UserCreatorTypedDict):
        email = data.get('email')
        self._user_repository.find_or_raise_by_email(email=email)

        username = data.get('username')
        self._user_repository.find_or_raise_by_username(username=username)
