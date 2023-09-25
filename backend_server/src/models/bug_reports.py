from typing import Any, List
import datetime

from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func

from src.database.metadata import Base

from ..schemas.bug_reports import BugReportSchema



class BugReports(Base):
    __tablename__ = 'bug_reports'

    id: Mapped[int] = mapped_column(primary_key=True)

    author_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.id'))
    text: Mapped[str] = mapped_column(String(512))

    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    def get_schema(self) -> BugReportSchema:
        return BugReportSchema(
            id=self.id,
            author_id=self.author_id,
            text=self.text,
            created_at=self.created_at,
        )
