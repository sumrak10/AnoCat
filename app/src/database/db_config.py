from pydantic import BaseModel

class DBSettings(BaseModel):
    HOST:str = "db"
    PORT:str = "5432"
    NAME:str = "anocat_db"
    USER:str = "postgres"
    PASS:str = "vErY26hhh03PSWD"


db_settings = DBSettings()