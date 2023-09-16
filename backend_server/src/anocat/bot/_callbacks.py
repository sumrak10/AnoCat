from aiogram import types
from aiogram.types import InlineKeyboardButton

from ..main import bot




class MyAnswersCallBack:
    callback_data: str = "mails_mine"
    button_text: str = "📝 Мои письма"
    @classmethod
    async def handler(cls, callback_query: types.CallbackQuery, callback_data: dict):
        pass

    @classmethod
    def keyboard(cls):
        return InlineKeyboardButton(cls.button_text, callback_data=cls.callback_data)

class MyTopicsCallBack:
    callback_data: str = "topics_mine"
    button_text: str = "💬 Мои топики"
    @classmethod
    async def handler(cls, callback_query: types.CallbackQuery, callback_data: dict):
        pass

    @classmethod
    def keyboard(cls):
        return InlineKeyboardButton(cls.button_text, callback_data=cls.callback_data)

class SettingsCallBack:
    callback_data: str = "settings"
    button_text: str = "⚙️ Настройки"
    @classmethod
    async def handler(cls, callback_query: types.CallbackQuery, callback_data: dict):
        pass

    @classmethod
    def keyboard(cls):
        return InlineKeyboardButton(cls.button_text, callback_data=cls.callback_data)