import logging

from aiogram import Bot
from aiogram import types
from aiogram import Router
from aiogram import F
from aiogram.filters.command import Command
from aiogram.utils.keyboard import (
    InlineKeyboardBuilder,\
    InlineKeyboardMarkup
)

from src.services.mails import MailsService

from . import callback_data
from . import keyboards


router = Router(name=callback_data.settings.name)



@router.message(Command(callback_data.settings.name))
async def message_handler(msg: types.Message, bot: Bot):
    await bot.send_message(
        chat_id=msg.from_user.id,
        text=await get_text(msg), 
        parse_mode="HTML", 
        reply_markup=await keyboard()
    )


@router.callback_query(
    callback_data.MenuItem.filter(F.name == callback_data.settings.name)
)
async def callback_handler(
    query: types.CallbackQuery, 
    callback_data: callback_data.MenuItem,
    bot: Bot
):
    await bot.edit_message_text(
        text=await get_text(query.message), 
        chat_id=query.message.chat.id, 
        message_id=query.message.message_id,
        parse_mode="HTML",
        reply_markup=await keyboard()
    )



async def get_text(msg: types.Message):
    mails = await MailsService.get_written_by_me(user_id=msg.from_user.id)
    if mails == []:
        return "Писем пока что нет! Создайте новый топик или \
            опубликуйте вашу ссылку в своих соц.сетях ;)"
    text = "Письма:\n"
    for mail in mails:
        text += f"Письмо: {mail.text}\n"

    return text

async def keyboard(web_app_link: str = '/'):
    kb_builder = InlineKeyboardBuilder()
    kb_builder.attach(InlineKeyboardBuilder.from_markup(InlineKeyboardMarkup(
        inline_keyboard=[
            [
                keyboards.main_menu_btn
            ],
            [
                keyboards.web_app_btn(web_app_link)
            ]
        ]
    )))

    return kb_builder.as_markup()