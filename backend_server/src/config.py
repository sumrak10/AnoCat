import logging, logging.config

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=True, 
        env_prefix='BACKEND_SERVER__'
    )

    DEBUG: bool = False
    HOST: str = 'https://7b76-84-54-80-187.ngrok-free.app'
    PORT: int = '8000'
    STATIC_URL: str = '/static'
    MEDIA_SERVER_HOST: str = 'http://localhost:8001'

settings = Settings()

# logging.config.fileConfig("logging.ini")
# logger = logging.getLogger('appLogger')