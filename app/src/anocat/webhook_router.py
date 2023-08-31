import logging

from fastapi import APIRouter
from .main import bot, dp
from .FastAPIRequestHandler import FastAPIRequestHandler
from .web_app.router import router as web_app_router
from .config import settings
from ..config import settings as app_settings



router = APIRouter(
    prefix=settings.APP_PREFIX, 
    tags=['bot']
)
router.include_router(web_app_router)

WEBHOOK_URL = f"{settings.WEBHOOK_URL}{settings.APP_PREFIX}/{settings.TOKEN}"
webhook_requests_handler = FastAPIRequestHandler(
    dispatcher=dp, 
    bot=bot, 
    webhook_url=WEBHOOK_URL,
    webhook_path=f"/{settings.TOKEN}",
    handle_in_background=True
)
router.include_router(webhook_requests_handler.get_router())


# @router.post(f"/{settings.TOKEN}")
# async def handle(request):
#     bot = await webhook_requests_handler.resolve_bot(request)
#     if webhook_requests_handler.handle_in_background:
#         return await webhook_requests_handler._handle_request_background(bot=bot, request=request)
#     return await webhook_requests_handler._handle_request(bot=bot, request=request)
# async def bot_webhook(update: dict):
#     # Dispatcher.set_current(dp)
#     # Bot.set_current(bot)
#     # await dp.process_update(types.Update(**update))
#     await dp.feed_update(bot=bot, update=types.Update(**update))

# # @router.on_event("startup")
# async def on_startup():
#     logging.info("Bot on startup event")
#     webhook_info = await bot.get_webhook_info()
#     if webhook_info.url != WEBHOOK_URL:
#         if app_settings.NOT_SEND_CERT:
#             res = await bot.set_webhook(
#                 url=WEBHOOK_URL,
#             )
#         else:
#             f = open('rootCA.pem', 'rb')
#             cert = f.read()
#             f.close()
#             res = await bot.set_webhook(
#                 url=WEBHOOK_URL,
#                 certificate=cert
#             )
#         logging.info("Bot webhook setted.")
#     else:
#         logging.WARN("Bot webhook not setted")
