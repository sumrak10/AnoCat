from time import perf_counter


from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.requests import Request



async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    return response

class ProcessTimeHeaderMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app,
    ) -> None:
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        start_time = perf_counter()
        response = await call_next(request)
        response.headers["X-Process-Time"] = str(round(float(perf_counter() - start_time),4))
        return response