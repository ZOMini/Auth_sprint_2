from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    test_host: str = Field(...)
    JAEGER_HOST: str = Field('jaeger')
    JAEGER_PORT: str = Field('6831')

    class Config:
        env_file = '.env'


settings = Settings()
