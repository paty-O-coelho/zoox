from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import Type

class Settings(BaseSettings):
    """
    Configuraçoes gerais do projeto
    """
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:12345678@localhost:5432/zoox"
    DBBaseModel: Type = declarative_base()

    class Config:
        case_sensitive = True

settings = Settings()