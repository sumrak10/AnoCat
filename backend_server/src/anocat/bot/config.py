import logging, logging.config

from pydantic_settings import BaseSettings, SettingsConfigDict

from src.config import settings as app_settings

class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_prefix='BOT__')

    TOKEN: str = '6558422249:AAEKtj3qMXlhO8T9h61McKsore2jkHabgXs'
    APP_PREFIX: str = "/bot"
    
    WEBHOOK_URL: str =  f"{app_settings.HOST}"


settings = Settings()

# logging.config.fileConfig("logging.ini")
# logger = logging.getLogger('botLogger')