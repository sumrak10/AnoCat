from fastapi import APIRouter

from .FastAPIRequestHandler import FastAPIRequestHandler

from .config import settings
from .bot import bot
from .dispatcher import dp


router = APIRouter(
    prefix=settings.APP_PREFIX, 
    tags=[settings.APP_PREFIX[1:]]
)


WEBHOOK_URL = f"{settings.WEBHOOK_URL}{settings.APP_PREFIX}/anocat"
webhook_requests_handler = FastAPIRequestHandler(
    dispatcher=dp, 
    bot=bot, 
    webhook_url=WEBHOOK_URL,
    webhook_path="/anocat",
    handle_in_background=False
)
router.include_router(webhook_requests_handler.get_router())