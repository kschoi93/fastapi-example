from fastapi import Depends
from sqlalchemy.orm import Session

from core.database import get_db


def get_user_profile_repository(db: Session = Depends(get_db)):
    return UserProfileRepository(db)


class UserProfileRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_user_id(self, user_id: int):
        ...
