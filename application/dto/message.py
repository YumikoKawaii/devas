from typing import Optional, List, Any
from datetime import datetime
from application.pkg.repository.models import Message
from application.dto.base import CamelBaseModel


class GetMessagesRequest:
    conversation_id: Optional[str]
    sender: Optional[str]
    page: Optional[int]
    page_size: Optional[int]
    start_action_time: Optional[datetime]
    end_action_time: Optional[datetime]


class GetMessagesResponse(CamelBaseModel):
    messages: Optional[List[Message]]

