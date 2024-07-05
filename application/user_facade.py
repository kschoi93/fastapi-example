from fastapi import Depends

from domain.user.dto.user import User
from domain.user_profile.user_profile_service import UserProfileService, get_user_profile_service
from domain.user.user_service import UserService, get_user_service


def get_user_facade(
        user_service: UserService = Depends(get_user_service),
        user_profile_service: UserProfileService = Depends(get_user_profile_service),
):
    return UserFacade(user_service, user_profile_service)


class UserFacade:
    def __init__(self, user_service: UserService, user_profile_service: UserProfileService):
        self.user_service = user_service
        self.user_profile_service = user_profile_service

    def sign_up(self, user_name: str):
        user: User | None = self.user_service.create(user_name)
        print(user)
        self.user_profile_service.get_by_user_id(user.id)
