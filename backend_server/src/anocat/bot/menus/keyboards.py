from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import InlineKeyboardButton

from src.config import settings as app_settings

from . import callback_data



def web_app_btn(link: str = '/'):
    return InlineKeyboardButton(
        text='Открыть в окне', 
        web_app=WebAppInfo(url=f"{app_settings.HOST}/bot/web_app{link}")
    )
settings_btn = InlineKeyboardButton(
    text='⚙️ Настройки', 
    callback_data=callback_data.settings.pack()
)
main_menu_btn = InlineKeyboardButton(
    text="Главное меню", 
    callback_data=callback_data.main_menu.pack()
)
