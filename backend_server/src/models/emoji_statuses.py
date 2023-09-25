from typing import Any, List
from datetime import datetime
from pydantic import BaseModel

from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func

from src.database.metadata import Base

from ..schemas.emoji_statuses import EmojiStatusSchema



class EmojiStatuses(Base):
    __tablename__ = 'emoji_statuses'

    id: Mapped[int] = mapped_column(primary_key=True)

    emoji: Mapped[str] = mapped_column(String(1))

    def get_schema(self) -> EmojiStatusSchema:
        return EmojiStatusSchema(
            id=self.id,
            emoji=self.emoji
        )
