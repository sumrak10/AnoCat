from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse

from .rndpath.router import router as rndpath_router
from .rndpath.services import RndPathService

from .middlewares import ProcessTimeHeaderMiddleware


app = FastAPI()

app.include_router(rndpath_router)

# app.add_middleware(ProcessTimeHeaderMiddleware)


@app.get("/{link}")
async def get_file(link: str):
    match link:
        case s if s.startswith('rnd'):
            try:
                return FileResponse(path=RndPathService.from_link_to_path(link[3:]))
            except FileNotFoundError:
                pass
        case s if s.startswith('abs'):
            pass
    return JSONResponse(content={"message":"Not found"}, status_code=404)