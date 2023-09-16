from aiogram.dispatcher.dispatcher import Dispatcher

from .ag_router import router as main_router
from .menus.main_menu import router as main_menu_router
from .menus.mails_by_me import router as mails_by_me_router
from .menus.mails_for_me import router as mails_for_me_router

# storage = RedisStorage2(host="localhost", port=6379)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)
dp = Dispatcher()

dp.include_router(main_router)

dp.include_router(main_menu_router)
dp.include_router(mails_by_me_router)
dp.include_router(mails_for_me_router)
