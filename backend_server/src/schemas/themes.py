from pydantic import BaseModel


class ThemeSchema(BaseModel):
    background_image: str
    bg_color: str
    text_color: str
    hint_color: str
    link_color: str
    button_color: str
    button_text_color: str
    secondary_bg_color: str