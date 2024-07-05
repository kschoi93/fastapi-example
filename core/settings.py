import os
from functools import lru_cache
from urllib import parse

from pydantic import PostgresDsn, field_validator
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import SettingsConfigDict, BaseSettings

env = os.getenv("ENV", "dev")
env_file = ".env"
if env == "prod":
    env_file = ".env.prod"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=True,
        env_file=env_file,
        env_file_encoding="utf-8",
    )
    API_STR: str = "/api"

    DB_TYPE: str
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int

    SQLALCHEMY_DATABASE_URI: None | str = None

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    @classmethod
    def assemble_db_connection(cls, v: None | str, info: ValidationInfo) -> any:
        data: dict[str, any] = info.data
        if isinstance(v, str):
            return v
        if env == "test":
            return "sqlite:///./test.db"
        postgresql_dsn: PostgresDsn = PostgresDsn.build(
            scheme="postgresql"
            if data.get("DB_TYPE") == "postgresql"
            else data.get("DB_TYPE"),
            username=data.get("DB_USER"),
            password=parse.quote_plus(data.get("DB_PASSWORD")),
            host=data.get("DB_HOST"),
            port=data.get("DB_PORT"),
            path=f"{data.get('DB_NAME') or ''}",
            # query="options=-csearch_path=",
        )
        return postgresql_dsn.unicode_string()


settings = Settings()
