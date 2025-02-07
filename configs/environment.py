import os
from functools import lru_cache

from pydantic import BaseSettings


@lru_cache
def get_env_filename() -> str:
    runtime_env = os.getenv("ENV")
    return f".env.{runtime_env}" if runtime_env else ".env"


class EnvironmentSettings(BaseSettings):
    API_VERSION: str
    APP_NAME: str
    DATABASE_DIALECT: str
    DATABASE_HOSTNAME: str
    DATABASE_NAME: str
    DATABASE_PASSWORD: str
    DATABASE_PORT: int
    DATABASE_USERNAME: str
    DEBUG_MODE: bool
    NEXTAUTH_SECRET: str
    ENV: str

    class Config:
        env_file = get_env_filename()
        env_file_encoding = "utf-8"


@lru_cache
def get_environment_variables() -> EnvironmentSettings:
    return EnvironmentSettings()
