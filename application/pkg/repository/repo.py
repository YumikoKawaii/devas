from typing import List
from datetime import datetime
import models
import sqlalchemy.engine.base
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy import select
from settings import settings


class IRepository:
    def get_messages(self, conditions: models.GetMessagesFilter) -> List[models.Message]:
        pass


class Repository(IRepository):
    connection: sqlalchemy.engine.base.Connection

    def __init__(self):
        connection_string = f'mysql+mysqlconnector://{settings.MYSQL_USERNAME}:{settings.MYSQL_PASSWORD}@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.MYSQL_DATABASE}'
        engine = create_engine(connection_string)
        connection = engine.connect()
        self.connection = connection

    def get_messages(self, conditions: models.GetMessagesFilter) -> List[models.Message]:
        stmt = select(models.Message)
        messages = self.connection.scalars(stmt)
        print(messages)
        return []
        pass

