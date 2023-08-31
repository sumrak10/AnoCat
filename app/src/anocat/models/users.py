from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship

from src.database.database_metadata import Base

from ..schemas.users import UserSchema



class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)

    emoji_status: Mapped[str] = mapped_column(String(1))
    name: Mapped[str] = mapped_column(String(128))
    anopoints: Mapped[int]

    topics: Mapped[list['Topics']] = relationship(back_populates="author")
    mails: Mapped[list['Mails']]  = relationship(back_populates="author")

    def get_schema(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            emoji_status=self.emoji_status,
            name=self.name,
            anopoints=self.anopoints
        )