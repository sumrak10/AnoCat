import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=True, 
        env_prefix='MEDIA_SERVER_FILES__'
    )

    BASE_DIR: str = os.getcwd().replace('\\','/')+'/files/'
    CHUNK_SIZE: int = 1024
    FOLDER_LENGTH: int = 2
    PATH_DEPTH: int = 3
    FILE_NAME_LENGTH: int = 12

settings = Settings()