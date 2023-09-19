from fastapi import APIRouter

from src.anocat.services.users import UsersService

from .config import settings



router = APIRouter(
    prefix=settings.APP_PREFIX,
    tags=[settings.APP_NAME]
)



@router.get('/user/{user_id}')
async def get_user(user_id: int):
    return await UsersService.get(user_id=user_id)

@router.get('/mails/{user_id}')
async def get_mails(user_id: int):
    pass