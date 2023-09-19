from typing import AsyncGenerator

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine

from .db_config import db_settings


engine = create_async_engine(
    f"postgresql+asyncpg://{db_settings.USER}:{db_settings.PASS}@{db_settings.HOST}:{db_settings.PORT}/{db_settings.NAME}", 
    echo=True
)

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)




async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


