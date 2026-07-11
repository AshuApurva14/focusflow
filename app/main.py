from fastapi import FastAPI

from app.core.config import settings

from app.api.v1.router import api_router

from app.exceptions.handlers import generic_exception_handler



app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION
)

app.include_router(
    api_router,
    prefix=settings.API_PREFIX
)

app.add_exception_handler(
    Exception, generic_exception_handler
)