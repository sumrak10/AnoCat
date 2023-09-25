import datetime

from pydantic import BaseModel


class BugReportSchema(BaseModel):
    id: int
    author_id: int
    text: str
    created_at: datetime.datetime