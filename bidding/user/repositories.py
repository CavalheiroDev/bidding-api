from bidding.user.contracts import IUserRepository
from bidding.user.types import UserCreatorTypedDict


class PostgresUserRepository(IUserRepository):

    def create_user(self, *, data: UserCreatorTypedDict):
        password = data.pop('password')
        user = self.model(**data)
        user.set_password(password)
        user.save()
        return user
