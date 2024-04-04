import os
import secrets

from dotenv import load_dotenv
from datetime import timedelta
from dataclasses import dataclass


load_dotenv()


@dataclass
class Settings:
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "MOVIE-COMPILATION-SERVICE"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE: timedelta = timedelta(minutes=15)
    REFRESH_TOKEN_EXPIRE: timedelta = timedelta(days=1)

    OMDB_KEY:            str = os.getenv("OMDB_KEY")

    POSTGRES_USER:       str = os.getenv('POSTGRES_USER')
    POSTGRES_PASSWORD:   str = os.getenv('POSTGRES_PASSWORD')
    POSTGRES_DB:         str = os.getenv('POSTGRES_DB')
    POSTGRES_PORT:       int = os.getenv('POSTGRES_PORT', 5432)
    POSTGRES_SERVER:     str = os.getenv('POSTGRES_SERVER')

    DATABASE_URL:        str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    class Config:
        env_file = ".env"


settings = Settings()
