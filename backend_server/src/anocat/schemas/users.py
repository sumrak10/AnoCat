from typing import Any

from pydantic import BaseModel



class UserSchema(BaseModel):
    id: int
    emoji_status:str
    name: str
    anopoints: int

class UserSchemaAdd(BaseModel):
    id: int
    name: str

class UserSchemaEdit(BaseModel):
    emoji_status:str | None
    name: str | None
    settings: dict[str, Any]