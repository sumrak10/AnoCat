from typing import Optional
from datetime import datetime

from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy import func

from src.database.database_metadata import Base

from ..schemas.topics import TopicSchema



class Topics(Base):
    __tablename__ = 'topics'

    id: Mapped[int] = mapped_column(primary_key=True)

    author_id: Mapped[int] = mapped_column(BigInteger, 
        ForeignKey("users.id", ondelete="CASCADE")
    )

    text: Mapped[str] = mapped_column(String(256))
    pinned: Mapped[bool] = mapped_column(default=False)
    prio: Mapped[Optional[int]]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    def get_schema(self) -> TopicSchema:
        return TopicSchema(
            id=self.id,
            author_id=self.author_id,
            text=self.text,
            pinned=self.pinned,
            prio=self.prio
        )