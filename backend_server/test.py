import asyncio

from sqlalchemy import select, update
from sqlalchemy.orm import joinedload, selectinload, subqueryload

from src.models import *
from src.schemas.users import UserSchema

from src.database.database import async_session_maker

async def get_user(*joins, **filters):
    async with async_session_maker() as session:
        stmt = select(Users, *joins).filter_by(**filters)
        for i in joins:
            stmt.join(
                i
            )
        res = await session.execute(stmt)
        res = res.scalars().unique().all()
        await session.commit()
    # return UserSchema.model_validate(res, from_attributes=True)
    return [r.__dict__ for r in res]

async def main():
    user = await get_user(Topics, Themes, id=2032860694)
    print(user)


asyncio.run(main())