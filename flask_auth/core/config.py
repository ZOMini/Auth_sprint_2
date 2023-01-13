import logging
from datetime import timedelta

from flask import Flask
from flask_jwt_extended import JWTManager
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    POSTGRES_DB: str = Field(...)
    POSTGRES_USER: str = Field(...)
    POSTGRES_PASSWORD: str = Field(...)
    POSTGRES_HOST: str = Field(...)
    DB_DOCKER_HOST: str = Field(...) 
    POSTGRES_PORT: int = Field(...)
    REDIS_HOST: str = Field(...)
    REDIS_PORT: int = Field(...)
    REDIS_URL: str = Field(...)
    FLASK_SECRET_KEY: str = Field(...)
    JWT_SECRET_KEY: str = Field(...)
    DEBUG: bool = Field(...)
    JWT_ACCESS_TOKEN_EXPIRES: int = Field(...)  # Часов
    JWT_REFRESH_TOKEN_EXPIRES: int = Field(...)  # Дней
    THROTTLING: int = Field(...)  # Секунд
    SALT_PASSWORD: str = Field(...)
    SUPERUSER_NAME: str = Field(...) 
    SUPERUSER_EMAIL: str = Field(...) 
    SUPERUSER_PASSWORD: str = Field(...)
    TESTS: bool = Field(False)

    class Config:
        env_file = '../.env'
        env_file_encoding = 'utf-8'

settings = Settings()

ACCESS_EXPIRES = timedelta(hours=settings.JWT_ACCESS_TOKEN_EXPIRES)
REFRESH_EXPIRES = timedelta(days=settings.JWT_REFRESH_TOKEN_EXPIRES)
THROTTLING = timedelta(seconds=settings.THROTTLING)
TESTS = settings.TESTS

app = Flask(__name__)
app.config['DEBUG'] = settings.DEBUG
app.config['SECRET_KEY'] = settings.FLASK_SECRET_KEY
app.config['JWT_SECRET_KEY'] = settings.JWT_SECRET_KEY
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = ACCESS_EXPIRES
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = REFRESH_EXPIRES
jwt = JWTManager(app)
