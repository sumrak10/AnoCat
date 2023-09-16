from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_prefix='MEDIA_SERVER__')

    DEBUG: bool = True
    HOST: str = 'http://localhost'
    PORT: int = 8001

settings = Settings()