from ..schemas.users import UserSchema, UserSchemaEdit
from ..schemas.topics import TopicSchemaAdd
from ..utils.unitofwork import IUnitOfWork, UnitOfWork


class UsersService:
    @classmethod
    async def register(cls, 
        id: int, 
        name: str , 
        first_topic_text: str = "Задавайте любые вопросы :)", 
        uow: IUnitOfWork = UnitOfWork()
    ):
        user = UserSchema(
            id=id,
            emoji_status="🐈",
            name=name,
            anopoints=0
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
            # await uow.commit()

    @classmethod
    async def get(cls, user_id:int, uow: IUnitOfWork = UnitOfWork()) -> UserSchema:
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