from typing import Any, List
import datetime

from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func

from src.database.metadata import Base

from ..schemas.users import UserSchema



class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    # main fields
    name: Mapped[str] = mapped_column(String(16))
    anon_name: Mapped[str] = mapped_column(String(16), default='Аноним')
    avatar: Mapped[str] = mapped_column(String(64))
    anon_avatar: Mapped[str] = mapped_column(String(64))
    anopoints: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=func.now())


    # supp fields
    сompetence_in_reporting_violations: Mapped[int] = mapped_column(default=0)
    deleted: Mapped[bool] = mapped_column(default=False)
    banned_until_datetime: Mapped[datetime.datetime] = mapped_column(nullable=True)

    # relations fields
    emoji_status_id: Mapped[int] = mapped_column(ForeignKey('emoji_statuses.id'), nullable=True)
    theme_id: Mapped[int] = mapped_column(ForeignKey('themes.id'), default=1)

    # notifications
    disable_mails_notifications: Mapped[bool] = mapped_column(default=False)
    disable_answers_notifications: Mapped[bool] = mapped_column(default=False)

    # appearance
    adaptive_mode: Mapped[bool] = mapped_column(default=False) # Тема как в телеграм
    always_open_expanded: Mapped[bool] = mapped_column(default=False) # Всегда открывать на всю высоту
    disable_tips: Mapped[bool] = mapped_column(default=False)

    # privacy
    mails_default_anonymous: Mapped[bool] = mapped_column(default=True)
    hide_mail_text_in_notification: Mapped[bool] = mapped_column(default=False)
    hide_mail_author_name_in_notification: Mapped[bool] = mapped_column(default=False)
    black_words: Mapped[str] = mapped_column(default='')

    def get_schema(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            name=self.name,
            anon_name=self.anon_name,
            avatar=self.avatar,
            anon_avatar=self.anon_avatar,
            anopoints=self.anopoints,
            created_at=self.created_at,

            сompetence_in_reporting_violations=self.сompetence_in_reporting_violations,
            deleted=self.deleted,
            banned_until_datetime=self.banned_until_datetime,
            
            disable_mails_notifications=self.disable_mails_notifications,
            disable_answers_notifications=self.disable_answers_notifications,

            adaptive_mode=self.adaptive_mode,
            always_open_expanded=self.always_open_expanded,
            disable_tips=self.disable_tips,

            mails_default_anonymous=self.mails_default_anonymous,
            hide_mail_text_in_notification=self.hide_mail_text_in_notification,
            hide_mail_author_name_in_notification=self.hide_mail_author_name_in_notification,
            black_words=self.black_words,
        )