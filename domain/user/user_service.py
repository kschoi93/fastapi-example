from fastapi import Depends

from domain.user.dto.user import User
from repository.user.user_entity import UserEntity
from repository.user.user_repository import UserRepository, get_user_repository


def get_user_service(user_repository: UserRepository = Depends(get_user_repository)):
    return UserService(user_repository)


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create(self, user_name: str) -> User:
        user_entity = UserEntity(user_name=user_name)
        return self.user_repository.create(user_entity)
