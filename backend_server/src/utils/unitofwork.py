from abc import ABC, abstractmethod
from typing import Type

from src.database.database import async_session_maker

from ..repositories.users import UsersRepository
from ..repositories.topics import TopicsRepository
from ..repositories.mails import MailsRepository
from ..repositories.answers import AnswersRepository
from ..repositories.topic_of_day import TopicOfDayRepository

# https://github1s.com/cosmicpython/code/tree/chapter_06_uow
class IUnitOfWork(ABC):
    users: Type[UsersRepository]
    topics: Type[TopicsRepository]
    mails: Type[MailsRepository]
    answers: Type[AnswersRepository]
    topic_of_day: Type[TopicOfDayRepository]
    
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    async def __aenter__(self):
        ...

    @abstractmethod
    async def __aexit__(self, *args):
        ...

    @abstractmethod
    async def commit(self):
        ...

    @abstractmethod
    async def rollback(self):
        ...


class UnitOfWork:
    def __init__(self):
        self.session_factory = async_session_maker

    async def __aenter__(self):
        self.session = self.session_factory()

        self.users = UsersRepository(self.session)
        self.topics = TopicsRepository(self.session)
        self.mails = MailsRepository(self.session)
        self.answers = AnswersRepository(self.session)
        self.topic_of_day = TopicOfDayRepository(self.session)

    async def __aexit__(self, *args):
        await self.rollback()
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()