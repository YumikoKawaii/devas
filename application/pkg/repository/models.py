from typing import Optional, Any
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(primary_key=True)
    conversation_id: Mapped[str]
    sender: Mapped[str]
    content: Mapped[str]
    action_time: Mapped[datetime]

    def __init__(self, conversation_id: str, sender: str, content: str, action_time: datetime, **kw: Any):
        super().__init__(**kw)
        self.conversation_id = conversation_id
        self.sender = sender
        self.content = content
        self.action_time = action_time


class GetMessagesFilter:
    id: Optional[int]
    conversation_id: Optional[str]
    sender: Optional[str]
    start_action_time: Optional[datetime]
    end_action_time: Optional[datetime]
    page: Optional[int]
    page_size: Optional[int]