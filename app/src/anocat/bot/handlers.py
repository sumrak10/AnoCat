from aiogram import types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo
from sqlalchemy.orm.exc import NoResultFound

from ..main import bot
from ..schemas.topic_of_day import TopicOfDaySchema
from ..services.topic_of_day import TopicOfDayService
from ..services.users import UsersService
from ..schemas.users import UserSchema
from .callbacks import MailsAllCallBack, MailsMineCallBack, TopicsMineCallBack, SettingsCallBack
from . import messages


async def start(msg: types.Message):
    try:
        user:UserSchema = await UsersService.get(user_id=msg.from_user.id)
    except NoResultFound:
        _name = msg.from_user.full_name[:128]
        user = UserSchema(
            id=msg.from_user.id,
            emoji_status="🆕",
            name=_name,
            anopoints=0
        )
        await UsersService.register(user)
        await bot.send_message(msg.from_user.id, messages.WELCOME_NEW_USER)

    topic_of_day:TopicOfDaySchema = await TopicOfDayService.get_today_topic_of_day()

    args = msg.get_args()

    greet_kb = InlineKeyboardMarkup()
    greet_kb.row(MailsAllCallBack.keyboard(), MailsMineCallBack.keyboard())
    greet_kb.add(TopicsMineCallBack.keyboard())
    greet_kb.add(SettingsCallBack.keyboard())
    greet_kb.add(InlineKeyboardButton('Открыть в приложении', web_app=WebAppInfo(url="https://36da-84-54-66-75.ngrok-free.app/bot/web_app/test")))

    await msg.reply(messages.build_main_menu_message(user, topic_of_day), parse_mode="HTML", reply_markup=greet_kb)



async def stop(msg: types.Message):
    await msg.reply(f"Good bye!")




# TODO УПРОСТИТЬ ВСЕ ДО ОБЫЧНОГО БОТА АНОНИМНЫХ ПИСЕМ