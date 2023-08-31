import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from src.database.database_metadata import Base

from ..schemas.topic_of_day import TopicOfDaySchema




class TopicOfDay(Base):
    __tablename__ = 'topic_of_day'

    id: Mapped[int] = mapped_column(primary_key=True)

    text: Mapped[str]
    date: Mapped[datetime.date]
    

    def get_schema(self) -> TopicOfDaySchema:
        return TopicOfDaySchema(
            id=self.id,
            text=self.text,
            date=self.date
        )