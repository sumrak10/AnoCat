import logging

from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher

from .config import settings
from .bot.aiogram_router import router



bot = Bot(token=settings.TOKEN)

# storage = RedisStorage2(host="localhost", port=6379)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)
dp = Dispatcher()

logging.warn(len(router.sub_routers))

dp.include_router(router)
