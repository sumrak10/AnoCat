from typing import Optional, List
from datetime import datetime

from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy import func

from src.database.metadata import Base

from ..schemas.mails import MailSchema



class Mails(Base):
    __tablename__ = 'mails'

    id: Mapped[int] = mapped_column(BigInteger ,primary_key=True)

    # main fields
    text: Mapped[str] = mapped_column(String(256))
    read: Mapped[bool] = mapped_column(default=False)
    anonymous: Mapped[bool]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # supp fields
    deleted: Mapped[bool] = mapped_column(default=False)

    # relations fields
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id"))

    def get_schema(self) -> MailSchema:
        return MailSchema(
            id=self.id,
            author_id=self.author_id,
            topic_id=self.topic_id,
            text=self.text,
            anonymous=self.anonymous,
            created_at=self.created_at,
        )