from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column,relationship
from sqlalchemy import ForeignKey

from src.database.database_metadata import Base

from ..schemas.mails import MailSchema



class Mails(Base):
    __tablename__ = 'mails'

    id: Mapped[int] = mapped_column(primary_key=True)

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    author: Mapped['Users'] = relationship(back_populates="mails")

    its_answer: Mapped[bool]

    topic_id: Mapped[Optional[int]] = mapped_column(ForeignKey("topics.id", ondelete="CASCADE"))
    topic: Mapped['Topics'] = relationship(back_populates="mails")

    mail_id: Mapped[Optional[int]] = mapped_column(ForeignKey("mails.id", ondelete="CASCADE"))
    mail: Mapped['Mails'] = relationship(back_populates="answers")

    answers: Mapped[list['Mails']] = relationship(back_populates="mail")

    text: Mapped[str]
    

    def get_schema(self) -> MailSchema:
        return MailSchema(
            id=self.id,
            author_id=self.author_id,
            its_answer=self.its_answer,
            mail_id=self.mail_id,
            text=self.text
        )