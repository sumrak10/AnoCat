from ..schemas.users import UserSchema
from ..schemas.topic_of_day import TopicOfDaySchema

WELCOME_NEW_USER = "Привет, я тебя не видел раньше, а тут всякие инструкции для новых юзеров и тд и тп !"

def build_main_menu_message(user: UserSchema, topic_of_day: TopicOfDaySchema):
    return f"\
{user.emoji_status} Пользователь: <a href='t.me/https://t.me/anocatbot?start=user__{user.id}'>{user.name}</a>\n\
📊 Рейтинг: #12345 ({user.anopoints} AP)\n\
✨ Топик дня: {topic_of_day.text}\n\
<a href='t.me/https://t.me/anocatbot?start=use_topic_of_day_template__{topic_of_day.id}'>➕ Использовать шаблон топика дня</a>\
    "