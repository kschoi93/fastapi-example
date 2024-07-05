from fastapi import FastAPI

from api import api_router
from core.database import engine
from repository.base_entity import BaseEntity

app = FastAPI()

app.include_router(api_router)

BaseEntity.metadata.create_all(bind=engine)