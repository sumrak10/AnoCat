from datetime import datetime

from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func

from src.database.database_metadata import Base

from ..schemas.users import UserSchema



class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    emoji_status: Mapped[str] = mapped_column(String(1))
    name: Mapped[str] = mapped_column(String(128))
    anopoints: Mapped[int]
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    def get_schema(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            emoji_status=self.emoji_status,
            name=self.name,
            anopoints=self.anopoints
        )