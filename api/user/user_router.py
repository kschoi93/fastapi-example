from fastapi import APIRouter, Depends

from application.user_facade import UserFacade, get_user_facade

router = APIRouter(prefix="/users")


@router.get("/")
def create(user_facade: UserFacade = Depends(get_user_facade)):
    user_name = "test"
    user_facade.sign_up(user_name)
