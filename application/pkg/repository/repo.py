import sqlalchemy.engine.base
from sqlalchemy import create_engine, Column, Integer, String
from settings import settings


class IRepository:
    def initialize(self):
        pass


class Repository(IRepository):
    connection: sqlalchemy.engine.base.Connection

    def __init__(self):
        connection_string = f'mysql+mysqlconnector://{settings.MYSQL_USERNAME}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DATABASE}'
        engine = create_engine(connection_string)
        connection = engine.connect()
        self.connection = connection

    def initialize(self):
        pass


