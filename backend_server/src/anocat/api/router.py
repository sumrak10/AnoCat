from fastapi import APIRouter

from .config import settings

from .v1.router import router as router_v1


router = APIRouter(
    prefix=settings.APP_PREFIX
)

router.include_router(router_v1)