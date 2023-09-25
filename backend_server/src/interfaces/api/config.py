import logging, logging.config

from pydantic_settings import BaseSettings, SettingsConfigDict

from src.config import settings as app_settings

class Settings(BaseSettings):
    APP_PREFIX: str = '/api'

settings = Settings()

# logging.config.fileConfig("logging.ini")
# logger = logging.getLogger('apiLogger')