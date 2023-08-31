from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_prefix='APP__', env_nested_delimiter='__')

    
    NOT_SEND_CERT:bool = True
    DEBUG:bool = False
    HOST:str
    PORT:int

settings = Settings()