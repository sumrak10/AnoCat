from ..schemas.answers import AnswerSchemaAdd
from ..utils.unitofwork import IUnitOfWork, UnitOfWork



class MailsService:
    @classmethod
    async def create(cls, answer:AnswerSchemaAdd, uow: IUnitOfWork = UnitOfWork()) -> None:
        async with uow:
            answer_id = await uow.answers.add_one(answer.model_dump())
            await uow.commit()

    @classmethod
    async def delete(cls, answer_id: int, uow: IUnitOfWork = UnitOfWork()) -> None:
        async with uow:
            await uow.answers.delete(id=answer_id)
            await uow.commit()