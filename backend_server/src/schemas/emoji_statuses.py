from pydantic import BaseModel


class EmojiStatusSchema(BaseModel):
    id: int
    emoji: str