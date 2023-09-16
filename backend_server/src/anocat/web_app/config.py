from pydantic_settings import BaseSettings, SettingsConfigDict

from src.config import settings as app_settings

class Settings(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True, env_prefix='WEB_APP__')

    APP_PREFIX: str = "/web_app"
    MAILS_FOR_ME_URL: str = "/mails_for_me"
    WEB_APP_URL: str = f"{app_settings.HOST}{APP_PREFIX}"

settings = Settings()