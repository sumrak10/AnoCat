from pydantic import BaseModel



class TopicSchema(BaseModel):
    id: int
    author_id:int
    text: str
    pinned: bool
    prio: int

class TopicSchemaAdd(BaseModel):
    author_id:int
    text: str
    pinned: bool
    prio: int