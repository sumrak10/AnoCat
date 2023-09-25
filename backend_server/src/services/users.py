from aiogram import types as ag_types
from aiohttp import ClientSession

from src.config import file_server_settings

from ..schemas.users import UserSchema, UserSchemaEdit, UserSchemaAdd
from ..schemas.topics import TopicSchemaAdd
from ..utils.unitofwork import IUnitOfWork, UnitOfWork


class UsersService:
    @classmethod
    async def register(cls, 
        id: int, 
        name: str , 
        photo: ag_types.File = None,
        first_topic_text: str = "Задавайте любые вопросы :)", 
        uow: IUnitOfWork = UnitOfWork()
    ):
        if photo is not None:
            async with ClientSession(trust_env=True) as session:
                async with session.post(
                    url=f"{file_server_settings.HOST}:{file_server_settings.PORT}/rndpath/save_file_from_telegram_api/", 
                    data={
                        "file_path": photo.file_path,
                        "ext": ".jpg"
                    }
                ) as response:
                    avatar = response.json()['link']
        else:
            avatar = 'absavatar.jpg'
        user = UserSchemaAdd(
            id=id,
            name=name,
            avatar=avatar,
            anon_avatar='absanonavatar.jpg'
        )
        topic = TopicSchemaAdd(
            author_id=user.id, 
            text=first_topic_text, 
            pinned=True, 
            prio=0
        )
        async with uow:
            await uow.users.add_one(user.model_dump())
            await uow.topics.add_one(topic.model_dump())
            await uow.commit()

    @classmethod
    async def get(cls, id:int, uow: IUnitOfWork = UnitOfWork()) -> UserSchema:
        async with uow:
            user = await uow.users.get_one(id=user_id)
            await uow.commit()
        return user

    @classmethod
    async def edit(cls, user_id: int,  user:UserSchemaEdit, uow: IUnitOfWork = UnitOfWork()):
        async with uow:
            await uow.users.edit_one(id=user_id, data=user.model_dump())
            await uow.commit()

    @classmethod
    async def add_anopoints(cls, user_id: int, anopoints: int = 1, uow: IUnitOfWork = UnitOfWork()):
        async with uow:
            user: UserSchema = await uow.users.get_one(id=user_id)
            await uow.users.edit_one(id=user_id, data={"anopoints":user.anopoints+anopoints})
            await uow.commit()