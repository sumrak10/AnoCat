from ..schemas.mails import MailSchemaAdd, MailSchema
from ..utils.unitofwork import IUnitOfWork, UnitOfWork



class MailsService:
    @classmethod
    async def create(cls, mail:MailSchemaAdd, uow: IUnitOfWork = UnitOfWork()) -> None:
        async with uow:
            mail_id = await uow.mails.add_one(mail.model_dump())
            await uow.commit()

    @classmethod
    async def delete(cls, mail_id:int, uow: IUnitOfWork = UnitOfWork()) -> None:
        async with uow:
            await uow.mails.delete(id=mail_id)

    @classmethod
    async def get_written_by_me(cls, user_id: int, uow: IUnitOfWork = UnitOfWork()) -> list[MailSchema]:
        async with uow:
            await uow.mails.get_all_with_filters(author_id=user_id)

    @classmethod
    async def get_written_to_me(cls, user_id: int, uow: IUnitOfWork = UnitOfWork()) -> list[MailSchema]:
        async with uow:
            topics = uow.topics.get_all_with_filters(author_id=user_id)
            mails = []
            for topic in topics:
                mails.append(uow.mails.get_all_with_filters(topic_id=topic.id))
            return mails