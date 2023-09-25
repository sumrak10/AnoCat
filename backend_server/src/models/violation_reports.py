from typing import Any, List
import datetime

from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func

from src.database.metadata import Base

from ..schemas.violation_reports import ViolationReportSchema



class ViolationReports(Base):
    __tablename__ = 'violation_reports'

    id: Mapped[int] = mapped_column(primary_key=True)

    author_id: Mapped[int] = mapped_column(BigInteger, ForeignKey('users.id'))
    text: Mapped[str]

    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())

    def get_schema(self) -> ViolationReportSchema:
        return ViolationReportSchema(
            id=self.id,
            author_id=self.author_id,
            violator_id=self.violator_id,
            created_at=self.created_at,
        )
