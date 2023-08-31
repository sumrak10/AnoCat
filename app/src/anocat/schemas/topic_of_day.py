import datetime

from pydantic import BaseModel



class TopicOfDaySchema(BaseModel):
    id: int
    text: str
    date: datetime.date

class TopicOfDaySchemaAdd(BaseModel):
    text: str
    date: datetime.date