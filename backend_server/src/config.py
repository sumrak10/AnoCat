from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=True, 
        env_prefix='BACKEND_SERVER__'
    )

    DEBUG: bool = False
    HOST: str
    PORT: int
    STATIC_URL: str = '/static'
    MEDIA_SERVER_HOST: str = 'http://localhost:8001'

settings = Settings()