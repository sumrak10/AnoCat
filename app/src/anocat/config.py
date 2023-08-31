from pydantic_settings import BaseSettings, SettingsConfigDict

from ..config import settings as app_settings

class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_prefix='BOT__')

    TOKEN: str
    APP_PREFIX: str = "/bot"
    WEBHOOK_URL: str =  f"{app_settings.HOST}"


settings = Settings()