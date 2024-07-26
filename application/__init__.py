from fastapi import FastAPI
from settings import settings


def initialize() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_TITLE
    )

    application.include_router(prefix="/api", )

    return application
