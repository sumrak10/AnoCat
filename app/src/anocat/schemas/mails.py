from pydantic import BaseModel

class MailSchema(BaseModel):
    id: int
    author_id:int
    its_answer: bool
    topic_id: int | None
    mail_id: int | None
    text: str

class MailSchemaAdd(BaseModel):
    its_answer: bool
    author_id:int
    topic_id: int | None
    mail_id:int | None
    text: str