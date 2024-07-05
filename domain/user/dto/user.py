from core.entity_to_model import EntityToModel


class User(EntityToModel):
    id: int
    user_name: str
