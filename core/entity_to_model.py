from pydantic import BaseModel, ConfigDict


class EntityToModel(BaseModel):
    model_config = ConfigDict(
        from_attributes=True,
    )