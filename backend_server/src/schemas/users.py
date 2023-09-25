from typing import Any, List
import datetime

from pydantic import BaseModel

from ..utils.types import Image

from .emoji_statuses import EmojiStatusSchema
from .themes import ThemeSchema
from .topics import TopicSchema


class UserSchema(BaseModel):
    id: int
    name: str
    anon_name: str
    avatar: Image
    anon_avatar: Image
    anopoints: int
    created_at: datetime.datetime

    сompetence_in_reporting_violations: int
    deleted: bool
    banned_until_datetime: datetime.datetime | None
    
    disable_mails_notifications: bool
    disable_answers_notifications: bool

    adaptive_mode: bool
    always_open_expanded: bool
    disable_tips: bool

    mails_default_anonymous: bool
    hide_mail_text_in_notification: bool
    hide_mail_author_name_in_notification: bool
    black_words: str

class UserSchemaAdd(BaseModel):
    id: int
    name: str
    avatar: str
    anon_avatar: str

class UserSchemaEdit(BaseModel):
    name: str | None
    anon_name: str | None
    avatar: str | None
    anon_avatar: str | None
    anopoints: int | None

    сompetence_in_reporting_violations: int | None
    deleted: bool | None
    banned_until_datetime: datetime.datetime | None

    emoji_status_id: int | None
    
    disable_mails_notifications: bool | None
    disable_answers_notifications: bool | None

    adaptive_mode: bool | None
    always_open_expanded: bool | None
    disable_tips: bool | None

    mails_default_anonymous: bool | None
    hide_mail_text_in_notification: bool | None
    hide_mail_author_name_in_notification: bool | None
    black_words: str | None