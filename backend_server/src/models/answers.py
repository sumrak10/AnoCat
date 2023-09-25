from datetime import datetime

from sqlalchemy import String, BigInteger
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy import func

from src.database.metadata import Base

from ..schemas.answers import AnswerSchema



class Answers(Base):
    __tablename__ = 'answers'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    # main fields
    text: Mapped[str] = mapped_column(String(128))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    # supp fields
    deleted: Mapped[bool] = mapped_column(default=False)

    # relations fields
    author_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"))
    
    mail_id: Mapped[int] = mapped_column(ForeignKey("mails.id", ondelete="CASCADE"))

    def get_schema(self) -> AnswerSchema:
        return AnswerSchema(
            id=self.id,
            author_id=self.author_id,
            mail_id=self.mail_id,
            topic_id=self.topic_id,
            text=self.text
        )