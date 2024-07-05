from fastapi import Depends

from repository.profile.user_profile_repository import UserProfileRepository, get_user_profile_repository


def get_user_profile_service(user_profile_repository: UserProfileRepository = Depends(get_user_profile_repository)):
    return UserProfileService(user_profile_repository)


class UserProfileService:
    def __init__(self, user_profile_repository: UserProfileRepository):
        self.user_profile_repository = user_profile_repository

    def get_by_user_id(self, user_id: int):
        self.user_profile_repository.get_by_user_id(user_id)
