from pydantic import BaseModel



class UserSchema(BaseModel):
    id: int
    emoji_status:str
    name: str
    anopoints: int

class UserSchemaEdit(BaseModel):
    emoji_status:str
    name: str