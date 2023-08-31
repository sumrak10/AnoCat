from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.database.database_metadata import Base

from ..schemas.answers import AnswerSchema



class Answers(Base):
    __tablename__ = 'answers'

    id: Mapped[int] = mapped_column(primary_key=True)

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    author: Mapped['Users'] = relationship(back_populates="answers")
    
    mail_id: Mapped[int] = mapped_column(ForeignKey("mails.id", ondelete="CASCADE"))
    mail: Mapped['Mails'] = relationship(back_populates="answers")
    topic_id: Mapped[int] = mapped_column(ForeignKey("topics.id", ondelete="CASCADE"))
    topic: Mapped['Topics'] = relationship(back_populates="answers")

    text: Mapped[str]
    

    def get_schema(self) -> AnswerSchema:
        return AnswerSchema(
            id=self.id,
            author_id=self.author_id,
            mail_id=self.mail_id,
            topic_id=self.topic_id,
            text=self.text
        )