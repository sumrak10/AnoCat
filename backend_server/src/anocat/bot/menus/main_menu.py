import logging

from aiogram import Bot
from aiogram import types
from aiogram import Router
from aiogram import F
from aiogram.filters.command import Command
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils.keyboard import (
    InlineKeyboardButton,\
    InlineKeyboardBuilder,\
    InlineKeyboardMarkup
)

from src.anocat.web_app.config import settings as web_app_settings
from src.anocat.schemas.topic_of_day import TopicOfDaySchema
from src.anocat.services.topic_of_day import TopicOfDayService
from src.anocat.services.users import UsersService

from . import callback_data
from . import keyboards

router = Router(name=callback_data.main_menu.name)



@router.message(Command(callback_data.main_menu.name))
async def message_handler(msg: types.Message, bot: Bot):
    
    await bot.send_message(
        chat_id=msg.from_user.id,
        text=await get_text(msg.from_user.id), 
        parse_mode="HTML", 
        reply_markup=await keyboard(msg.from_user.id)
    )

@router.callback_query(
    callback_data.MenuItem.filter(F.name == callback_data.main_menu.name)
)
async def callback_handler(
    query: types.CallbackQuery, 
    callback_data: callback_data.MenuItem,
    bot: Bot
):
    await bot.edit_message_text(
        text=await get_text(query.message.chat.id), 
        chat_id=query.message.chat.id, 
        message_id=query.message.message_id,
        parse_mode="HTML",
        reply_markup=await keyboard(query.message.chat.id)
    )

async def get_text(user_id: int):
    user = await UsersService.get(user_id=user_id)

    topic_of_day:TopicOfDaySchema = await TopicOfDayService.get_today_topic_of_day()

    return f"<b>Главное меню:</b>\n\
{user.emoji_status} Пользователь: <a href='t.me/https://t.me/anocatbot?start=topics__{user.id}'>{user.name}</a>\n\
📊 Рейтинг: #12345 ({user.anopoints} AP)\n\
✨ Топик дня: {topic_of_day.text}\n\
<a href='t.me/https://t.me/anocatbot?start=use_topic_of_day_template__{topic_of_day.id}'>\
➕ Создать по шаблону топика дня</a>"

async def keyboard(user_id):
    kb_builder = InlineKeyboardBuilder()
    kb_builder.attach(InlineKeyboardBuilder.from_markup(InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="💌 Все письма", 
                    callback_data=callback_data.mails_for_me.pack()
                ),
                InlineKeyboardButton(
                    text="✉️ Мои письма", 
                    callback_data=callback_data.mails_by_me.pack()
                )
            ],
            [
                InlineKeyboardButton(
                    text="☁️ Мои топики", 
                    callback_data=callback_data.my_topics.pack()
                )
            ],
            [
                keyboards.settings_btn
            ],
            [
                keyboards.web_app_btn()
            ]
        ]
    )))
    
    return kb_builder.as_markup()