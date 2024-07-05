from fastapi import APIRouter

from api.auth import auth_router
from api.user import user_router

api_router = APIRouter()

api_router.include_router(auth_router.router)
api_router.include_router(user_router.router)