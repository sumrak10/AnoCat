import logging

from aiogram import types
from aiogram import Router
from aiogram import F



router = Router(name='main')


@router.message(F.message)
async def start(msg: types.Message) -> None:
    logging.warn("handler triggered!!!")
    await msg.answer("Hello!")