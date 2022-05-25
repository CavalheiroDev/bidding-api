from bidding.user.types import UserCreatorTypedDict
from bidding.user.contracts import IUserRepository


class UserCreator:

    def __init__(self, user_repository: IUserRepository) -> None:
        self._user_repository = user_repository

    def create_user(self, data: UserCreatorTypedDict):
        user = self._user_repository.create_user(data=data)
        return user
