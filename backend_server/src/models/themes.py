from typing import List

from sqlalchemy import String, BigInteger, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.database.metadata import Base

class Themes(Base):
    __tablename__ = 'themes'

    id: Mapped[int] = mapped_column(primary_key=True)
    
    background_image: Mapped[str] = mapped_column(String(64))
    bg_color: Mapped[str] = mapped_column(String(6))
    text_color: Mapped[str] = mapped_column(String(6))
    hint_color: Mapped[str] = mapped_column(String(6))
    link_color: Mapped[str] = mapped_column(String(6))
    button_color: Mapped[str] = mapped_column(String(6))
    button_text_color: Mapped[str] = mapped_column(String(6))
    secondary_bg_color: Mapped[str] = mapped_column(String(6))