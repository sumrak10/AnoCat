from typing import Dict, Any

from fastapi.requests import Request



def request_context_processor(request: Request) -> Dict[str, Any]:
    return {
        "request": request,
    }