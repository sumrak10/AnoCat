from ..schemas.topics import TopicSchemaAdd
from ..utils.unitofwork import IUnitOfWork, UnitOfWork



class TopicsService:
    @classmethod
    async def create(cls, topic:TopicSchemaAdd,uow: IUnitOfWork = UnitOfWork()) -> None:
        async with uow:
            topic_id = await uow.topics.add_one(topic.model_dump())
            await uow.commit()

    @classmethod
    async def delete(cls, topic_id: int, uow: IUnitOfWork = UnitOfWork()) -> None:
        async with uow:
            await uow.answers.delete(topic_id=topic_id)
            await uow.mails.delete(topic_id=topic_id)
            await uow.topics.delete(id=topic_id)
            await uow.commit()