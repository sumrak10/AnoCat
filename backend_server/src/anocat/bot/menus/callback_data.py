from aiogram.filters.callback_data import CallbackData

class MenuItem(CallbackData, prefix="menu"):
    name:str

settings = MenuItem(name="settings")

main_menu = MenuItem(name="main_menu")

mails_for_me = MenuItem(name="mails_for_me")

mails_by_me = MenuItem(name="mails_by_me")

my_topics = MenuItem(name="my_topics")