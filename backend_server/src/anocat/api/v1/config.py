from pydantic_settings import BaseSettings, SettingsConfigDict

from src.config import settings as app_settings


class Settings(BaseSettings):
    APP_PREFIX: str = '/v1'
    APP_NAME: str = f"API {APP_PREFIX[1:]}"

settings = Settings()