from fastapi.templating import Jinja2Templates
from jinja2 import Environment

from . import context_processors
from . import filters
env = Environment()
templates = Jinja2Templates(
    directory="src/anocat/web_app/templates", 
    context_processors=[
        context_processors.request_context_processor
    ]
)
templates.env.globals['url'] = filters.url

TemplateResponse = templates.TemplateResponse