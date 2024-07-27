from fastapi import APIRouter
from . import message

router = APIRouter()
router.include_router(message.router, prefix='/messages')