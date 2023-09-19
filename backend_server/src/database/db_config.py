from pydantic_settings import BaseSettings, SettingsConfigDict

class DBSettings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=True, 
        env_prefix='DB__'
    )
    HOST:str = "localhost"
    PORT:str = "5432"
    NAME:str = "anocat_db"
    USER:str = "postgres"
    PASS:str = "vErY26hhh03PSWD"


db_settings = DBSettings()