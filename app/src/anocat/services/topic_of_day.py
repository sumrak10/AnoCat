import datetime

from ..schemas.topic_of_day import TopicOfDaySchemaAdd, TopicOfDaySchema
from ..utils.unitofwork import IUnitOfWork, UnitOfWork



class TopicOfDayService:
    @classmethod
    async def create(cls, topic_of_day:TopicOfDaySchemaAdd, uow: IUnitOfWork = UnitOfWork()) -> None:
        async with uow:
            topic_of_day_id = await uow.topic_of_day.add_one(topic_of_day.model_dump())
            await uow.commit()
    
    @classmethod
    async def get_today_topic_of_day(cls,uow: IUnitOfWork = UnitOfWork()) -> TopicOfDaySchema:
        async with uow:
            today = datetime.datetime.now()
            topic_of_day = await uow.topic_of_day.get_one(date=today.date())
            await uow.commit()
        return topic_of_day