import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(verbose=True)


class Settings(BaseSettings):
    PROJECT_TITLE: str = 'DEVAS'

    MYSQL_DATABASE: str = os.getenv('MYSQL_DATABASE', 'devas')
    MYSQL_USERNAME: str = os.getenv('MYSQL_USERNAME', 'operator')
    MYSQL_PASSWORD: str = os.getenv('MYSQL_PASSWORD', 'Yumiko1@')
    MYSQL_HOST: str = os.getenv('MYSQL_HOST', '127.0.0.1')
    MYSQL_PORT: int = os.getenv('MYSQL_PORT',3306)


settings = Settings()