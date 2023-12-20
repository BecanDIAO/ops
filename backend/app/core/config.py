import secrets
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl, field_validator, EmailStr, HttpUrl, MysqlDsn


class Settings(BaseSettings):
    PROJECT_NAME: str
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    ALGORITHM: str = "HS256"

    SERVER_NAME: str
    SERVER_PORT: int = 9999
    SERVER_HOST: AnyHttpUrl = "http://127.0.0.1"

    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

    ACCESS_TOKEN_HEADER_NAME: str = "Authorization"
    ACCESS_TOKEN_QUERY_STRING: bool = True

    DEBUG: bool = False

    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[MysqlDsn] = None
