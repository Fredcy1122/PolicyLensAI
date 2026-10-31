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

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / "backend" / ".env"
    )


settings = Settings()