from typing import List
from fastapi import APIRouter
from datetime import datetime
from application.dto.message import GetMessagesRequest, GetMessagesResponse, MessageInResponse
from application.dto.base import DataResponse

router = APIRouter()


@router.get('', response_model=DataResponse[GetMessagesResponse])
def get_messages():

    message = MessageInResponse(id=1, conversation_id='123',sender='123',content='12345', action_time=datetime(2024, 7, 27))

    data: List[MessageInResponse] = [message]

    return DataResponse().success_response(GetMessagesResponse(messages=data))

