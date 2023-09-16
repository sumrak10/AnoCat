
from sqlalchemy import select

from ..utils.repository import SQLAlchemyRepository
from ..models.mails import Mails
from ..models.users import Users



class MailsRepository(SQLAlchemyRepository):
    model = Mails

    async def get_all_with_filters_join_user(self, **filter_by) -> list[dict]:
        stmt = select(self.model.__table__, Users.__table__).filter_by(**filter_by) \
            .join(Users, (Users.id == self.model.author_id))
        res = await self.session.execute(stmt)
        res = res.mappings().all()
        return res

