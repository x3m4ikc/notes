from functools import lru_cache
from pydantic_settings import BaseSettings

from .settings.database_settings import DatabaseSettings, AsyncSessionmakerSettings


class Settings(BaseSettings):
    class Config:
        env_file = "../.env"

    postgres: DatabaseSettings = DatabaseSettings()
    async_sessionmaker: AsyncSessionmakerSettings = AsyncSessionmakerSettings()


@lru_cache
def get_settings():
    _settings = Settings()
    return _settings


settings = get_settings()
