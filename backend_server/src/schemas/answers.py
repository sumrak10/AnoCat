from pydantic import BaseModel



class AnswerSchema(BaseModel):
    id: int
    author_id:int
    mail_id: int
    topic_id:int
    text: str

class AnswerSchemaAdd(BaseModel):
    author_id:int
    mail_id: int
    topic_id:int
    text: str