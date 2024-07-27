from typing import List
from fastapi import APIRouter
from application.dto.message import GetMessagesRequest, GetMessagesResponse
from application.dto.base import DataResponse

router = APIRouter()


@router.get('', response_model=DataResponse[GetMessagesResponse])
def get_messages():
    return DataResponse().success_response(data=None)

