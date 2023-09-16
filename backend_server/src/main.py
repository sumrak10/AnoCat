from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .config import settings
from .anocat.bot.router import router as bot_router
from .anocat.web_app.router import router as web_app_router


app = FastAPI()


app.mount(
    settings.STATIC_URL, 
    StaticFiles(directory="src/anocat/web_app/static"), 
    name="static"
)


app.include_router(bot_router)
app.include_router(web_app_router)