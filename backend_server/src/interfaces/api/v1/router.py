from fastapi import APIRouter

from src.services.users import UsersService
from src.schemas.users import UserSchema

from src.services.topics import TopicsService
from src.schemas.topics import TopicSchema

from .config import settings



router = APIRouter(
    prefix=settings.APP_PREFIX,
    tags=[settings.APP_NAME]
)



@router.get(
    path='/user/{id}',
    response_model=UserSchema
)
async def get_user(id: int):
    return await UsersService.get(id)

@router.get(
    path='/topics/{id}',
    response_model=TopicSchema
)
async def get_topics(id: int):
    return await TopicsService.get_user_topics(id)
