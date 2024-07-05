from sqlalchemy.orm import Mapped, mapped_column

from repository.base_entity import BaseEntity


class UserEntity(BaseEntity):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_name: Mapped[str]
