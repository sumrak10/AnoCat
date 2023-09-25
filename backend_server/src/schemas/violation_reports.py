import datetime

from pydantic import BaseModel


class ViolationReportSchema(BaseModel):
    id: int
    author_id: int
    violator_id: int
    created_at: datetime.datetime