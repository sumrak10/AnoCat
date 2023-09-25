from time import perf_counter

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles

from .config import settings
from .interfaces.bot.router import router as bot_router
from .interfaces.web_app.router import router as web_app_router
from .interfaces.api.router import router as api_router

from .middlewares import ProcessTimeHeaderMiddleware

app = FastAPI()

app.add_middleware(ProcessTimeHeaderMiddleware)

app.mount(
    settings.STATIC_URL, 
    StaticFiles(directory="src/interfaces/web_app/static"), 
    name="static"
)

app.include_router(api_router)
app.include_router(bot_router)
app.include_router(web_app_router)