from ..schemas.mails import MailSchema, MailSchemaAdd
from ..utils.unitofwork import IUnitOfWork, UnitOfWork


class MailsService:
    @classmethod
    async def create(cls, mail:MailSchemaAdd, uow: IUnitOfWork = UnitOfWork()) -> None:
        async with uow:
            await uow.mails.add_one(mail.model_dump())
            await uow.commit()

    @classmethod
    async def delete(cls, mail_id:int, uow: IUnitOfWork = UnitOfWork()) -> None:
        async with uow:
            await uow.mails.edit_one(id=mail_id).update(deleted=True)
            await uow.commit()

    @classmethod
    async def get_written_by_me(cls, 
        user_id: int, 
        uow: IUnitOfWork = UnitOfWork()
    ) -> list[MailSchema]:
        async with uow:
            mails = await uow.mails.get_all_with_filters(author_id=user_id)
            await uow.commit()
        return mails

    @classmethod
    async def get_written_for_me(cls, 
        user_id: int, 
        uow: IUnitOfWork = UnitOfWork()
    ) -> list[dict]:
        async with uow:
            mails = []
            for topic_id in await uow.topics.get_attrs_with_filters(
                uow.topics.model.id,
                author_id=user_id
            ):
                for mail in await uow.mails.get_all_with_filters_join_user(
                    topic_id=topic_id
                ):
                    await cls.mark_as_read(mail_id=mail.id, uow=uow)
                    mails.append(mail)
            await uow.commit()
        return mails
    
    @classmethod
    async def mark_as_read(cls, 
        mail_id: int, 
        uow: IUnitOfWork = UnitOfWork()
    ) -> None:
        async with uow:
            await uow.mails.edit_one(
                id=mail_id,
                data={
                    uow.mails.model.c.read: True
                }
            )