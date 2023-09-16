import logging
import time

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi import BackgroundTasks
from fastapi import UploadFile
from fastapi.responses import FileResponse

from .services import files_service
from .config import settings

app = FastAPI()

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(round(float(process_time),10))
    return response

@app.post("/")
async def save_file(file: UploadFile, background_tasks: BackgroundTasks):
    logging.warn(file.size)
    link = await files_service.save_file(file,
        run_in_background=True,
        background_tasks=background_tasks
    )

    return {"message": "OK", "link": f"{settings.HOST}:{settings.PORT}/{link}"}


@app.get("/{link}")
async def file_save(link: str):
    return FileResponse(path=files_service.from_link_to_path(link),)