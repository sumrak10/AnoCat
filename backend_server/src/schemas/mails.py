from datetime import datetime

from pydantic import BaseModel

class MailSchema(BaseModel):
    id: int
    author_id:int
    topic_id: int
    text: str
    read: bool
    anonymous: bool
    created_at: datetime

class MailSchemaAdd(BaseModel):
    author_id:int
    topic_id: int
    text: str
    read: bool = False
    anonymous: bool
    created_at: datetime