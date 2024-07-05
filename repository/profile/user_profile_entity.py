from sqlalchemy.orm import Mapped, mapped_column

from repository.base_entity import BaseEntity


class UserProfileEntity(BaseEntity):
    __tablename__ = "user_profiles"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
