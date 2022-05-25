from bidding.user.repositories import PostgresUserRepository
from bidding.user.services.user_creator import UserCreator


def make_postgres_user_repository() -> PostgresUserRepository:
    return PostgresUserRepository()


def make_user_creator_service() -> UserCreator:
    return UserCreator(user_repository=make_postgres_user_repository())
