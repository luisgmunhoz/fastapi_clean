import os
from functools import lru_cache

from pydantic import BaseSettings


@lru_cache
def get_env_filename() -> str:
    runtime_env = os.getenv("ENV")
    return f".env.{runtime_env}" if runtime_env else ".env"


class EnvironmentSettings(BaseSettings):
    API_VERSION: str | None
    APP_NAME: str | None
    DATABASE_DIALECT: str | None
    DATABASE_HOSTNAME: str | None
    DATABASE_NAME: str | None
    DATABASE_PASSWORD: str | None
    DATABASE_PORT: int | None
    DATABASE_USERNAME: str | None
    DEBUG_MODE: bool | None
    ENV: str

    class Config:
        env_file = get_env_filename()
        env_file_encoding = "utf-8"


@lru_cache
def get_environment_variables() -> EnvironmentSettings:
    return EnvironmentSettings()
