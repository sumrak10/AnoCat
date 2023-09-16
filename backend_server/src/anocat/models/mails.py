from typing import Optional
from datetime import datetime

from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy import func

from src.database.database_metadata import Base

from ..schemas.mails import MailSchema



class Mails(Base):
    __tablename__ = 'mails'

    id: Mapped[int] = mapped_column(primary_key=True)

    author_id: Mapped[int] = mapped_column(BigInteger, 
        ForeignKey("users.id", ondelete="CASCADE")
    )
    topic_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("topics.id", ondelete="CASCADE"))

    text: Mapped[str] = mapped_column(String(256))
    read: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    deleted: Mapped[bool] = mapped_column(default=False)

    def get_schema(self) -> MailSchema:
        return MailSchema(
            id=self.id,
            author_id=self.author_id,
            topic_id=self.topic_id,
            text=self.text
        )