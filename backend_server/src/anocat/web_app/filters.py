from src.config import settings 

def url(name: str, path: str) -> str:
    urls = {
        "static": settings.STATIC_URL,
        "media": settings.MEDIA_SERVER_HOST
    }
    return f"{urls[name]}{path}"