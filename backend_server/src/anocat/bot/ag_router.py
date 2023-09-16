from aiogram import Bot
from aiogram import types
from aiogram import Router
from aiogram import F
from aiogram.filters.command import Command, CommandObject

from sqlalchemy.orm.exc import NoResultFound

from src.anocat.services.users import UsersService
from .menus.main_menu import message_handler as main_menu_message_handler

router = Router(name='main')


@router.message(Command('start'))
async def start(msg: types.Message, bot: Bot, command: CommandObject) -> None:
    try:
        user = await UsersService.get(user_id=msg.from_user.id)
    except NoResultFound:
        await UsersService.register(
            id=msg.from_user.id, 
            name=msg.from_user.full_name[:128]
        )
        await bot.send_message(
            msg.from_user.id, 
            "Привет, я тебя не видел раньше, \
            а тут всякие инструкции для новых юзеров и тд и тп !"
        )
    if command.args:
        msg.reply(command.args)
    await main_menu_message_handler(msg, bot)



@router.message(F.photo)
async def photo_handler(msg: types.Message) -> None:
    # await bot.send_photo(
    #     msg.from_user.id, 
    #     photo=types.FSInputFile(path='/app/src/anocat/bot/1.png')
    # )
    # file = await bot.get_file(msg.photo[0].file_id)
    # logging.warn(file.file_path)
    # await bot.send_photo(msg.from_user.id, photo = msg.photo[0].file_id)
    pass