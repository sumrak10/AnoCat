from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.database.database_metadata import Base

from ..schemas.topics import TopicSchema



class Topics(Base):
    __tablename__ = 'topics'

    id: Mapped[int] = mapped_column(primary_key=True)

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    author: Mapped['Users'] = relationship(back_populates="topics")

    text: Mapped[str]
    pinned: Mapped[bool] = mapped_column(default=False)
    prio: Mapped[Optional[int]]

    mails: Mapped[list['Mails']]  = relationship(back_populates="topic")

    def get_schema(self) -> TopicSchema:
        return TopicSchema(
            id=self.id,
            author_id=self.author_id,
            text=self.text,
            pinned=self.pinned,
            prio=self.prio
        )