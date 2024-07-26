import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(verbose=True)


class Settings(BaseSettings):
    PROJECT_TITLE: str = 'DEVAS'


settings = Settings()