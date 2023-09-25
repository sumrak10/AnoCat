import logging

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi import BackgroundTasks
from fastapi import UploadFile
from fastapi.responses import FileResponse, JSONResponse


from .services import RndPathService
from ..utils.input_file import URLInputFile

from ..config import settings

router = APIRouter(
    prefix='/rndpath'
)


@router.post("/")
async def save_file_from_bytes(file: UploadFile, background_tasks: BackgroundTasks):

    link = await RndPathService.save_file_from_bytes(file, background_tasks=background_tasks)

    return JSONResponse(content={"status": "OK", "url": f"{settings.HOST}:{settings.PORT}/rnd{link}", "link": link})


@router.post("/")
async def save_file_from_telegram_api(file_path: str, ext: str, background_tasks: BackgroundTasks):

    link = await RndPathService.save_file_from_telegram_api(file_path, background_tasks=background_tasks)

    return JSONResponse(content={"status": "OK", "url": f"{settings.HOST}:{settings.PORT}/rnd{link}", "link": link})