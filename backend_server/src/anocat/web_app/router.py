from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse

from src.anocat.services.mails import MailsService

from .jinja import TemplateResponse
from .config import settings
from .utils import validateInitData

router = APIRouter(
    prefix=settings.APP_PREFIX,
    tags=[settings.APP_PREFIX[1:]]
)

@router.get(settings.MAILS_FOR_ME_URL, response_class=HTMLResponse)
async def mails_for_me(request: Request, user_id: int):
    mails = await MailsService.get_written_for_me(user_id=user_id)
    return TemplateResponse(
        "pages/mails_for_me.html", 
        {
            "request": request,
            "test": "It's test text",
            "mails": mails
        }
    )

@router.get('/mail/{mail_id}')
async def delete_mail(mail_id: int):
    await MailsService.delete(mail_id=mail_id)


@router.post("/validateInitData")
async def validate_init_data(initData: dict):
    if not validateInitData(init_data=initData['initData']):
        return JSONResponse({"message":"bad"})
    return JSONResponse({"message":"ok"})

