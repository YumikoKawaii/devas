from fastapi import FastAPI
from settings import settings
from application.api.endpoints import router


def initialize() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_TITLE
    )

    application.include_router(prefix="/api", router=router)

    return application
