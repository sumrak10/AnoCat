import logging

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi import BackgroundTasks
from fastapi import UploadFile
from fastapi.responses import FileResponse, JSONResponse

from .services import RPathService
from .config import settings


router = APIRouter(
    prefix='/rpath'
)

@router.get("/test/{test}")
async def test(test:int):
    return {"test": test}

@router.post("/")
async def save_file(file: UploadFile, background_tasks: BackgroundTasks):
    link = await RPathService.save_file(
        file,
        run_in_background=True,
        background_tasks=background_tasks
    )

    return {"message": "OK", "url": f"{settings.HOST}:{settings.PORT}/r{link}", "link": link}


@router.get("/{link}")
async def get_file(link: str):
    if link[0] != 'r':
        return JSONResponse(content={"message":"Not found"}, status_code=404)
    return FileResponse(path=RPathService.from_link_to_path(link[1:]))