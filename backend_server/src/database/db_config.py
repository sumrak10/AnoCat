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
    DB_AND_DRIVER: str = "postgresql+asyncpg"
    @property
    def DSN(self):
        return f"{self.DB_AND_DRIVER}://{self.USER}:{self.PASS}@{self.HOST}:{self.PORT}/{self.NAME}"


db_settings = DBSettings()