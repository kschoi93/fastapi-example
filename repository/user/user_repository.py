from fastapi import Depends
from sqlalchemy.orm import Session

from core.database import get_db
from domain.user.dto.user import User
from repository.user.user_entity import UserEntity


def get_user_repository(db: Session = Depends(get_db)):
    return UserRepository(db)


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, user_entity: UserEntity) -> User:
        self.session.add(user_entity)
        self.session.commit()
        self.session.refresh(user_entity)
        return User.model_validate(user_entity)