from typing import Optional, List, Any
from datetime import datetime
from application.dto.base import CamelBaseModel


class GetMessagesRequest:
    conversation_id: Optional[str]
    sender: Optional[str]
    page: Optional[int]
    page_size: Optional[int]
    start_action_time: Optional[datetime]
    end_action_time: Optional[datetime]


class MessageInResponse(CamelBaseModel):
    id: int = ""
    conversation_id: str = ""
    sender: str = ""
    content: str = ""
    action_time: datetime = ""

    def __init__(self, id: int, conversation_id: str, sender: str, content: str, action_time: datetime):
        super().__init__()
        self.id = id
        self.conversation_id = conversation_id
        self.sender = sender
        self.content = content
        self.action_time = action_time


class GetMessagesResponse(CamelBaseModel):
    messages: Optional[List[MessageInResponse]] = []

    def __init__(self, messages: List[MessageInResponse]):
        super().__init__()
        self.messages = messages

