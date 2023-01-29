from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    TEST_URL: str = Field(...)
    REQUESTS_COUNT: int = Field(...)
    JWT: str = Field(...)

    class Config:
        env_file = '.env'


settings = Settings()
