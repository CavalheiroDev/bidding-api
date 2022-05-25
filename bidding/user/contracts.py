from bidding.user.models import User
from bidding.user.exceptions import UserNotFound
from bidding.user.types import UserCreatorTypedDict

from utils.contracts_repositories import Repositories


class IUserRepository(Repositories):
    model = User
    not_found_exception = UserNotFound

    def create_user(self, *, data: UserCreatorTypedDict):
        raise NotImplementedError()
