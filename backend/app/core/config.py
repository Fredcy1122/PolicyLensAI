from pathlib import Path

from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict
)

BASE_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    APP_NAME: str
    API_VERSION: str
    ENVIRONMENT: str
    AZURE_OPENAI_ENDPOINT: str

    AZURE_OPENAI_API_KEY: str

    AZURE_OPENAI_DEPLOYMENT: str

    AZURE_OPENAI_API_VERSION: str

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()