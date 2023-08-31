from aiogram import types
from aiogram.types import InlineKeyboardButton

from ..main import bot



class MyMailsCallBack:
    callback_data: str = "mails_all"
    button_text: str = "💌 Все письма"
    @classmethod
    async def handler(cls, callback_query: types.CallbackQuery):
        await bot.answer_callback_query(
            callback_query.id,
            text=f'{callback_query.as_json()}', 
            show_alert=True)

    @classmethod
    def keyboard(cls):
        return InlineKeyboardButton(cls.button_text, callback_data=cls.callback_data)

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