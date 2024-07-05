from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth")


@router.post("/token")
def login(from_data: OAuth2PasswordRequestForm = Depends()):
    return "asdf"
