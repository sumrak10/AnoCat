import logging
import asyncio
from typing import Any, Dict, Optional

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse
from fastapi import BackgroundTasks
from aiogram.methods import TelegramMethod
from aiogram import Bot, Dispatcher
from aiogram.dispatcher.dispatcher import Dispatcher
from aiogram.webhook.aiohttp_server import BaseRequestHandler


class FastAPIRequestHandler(BaseRequestHandler):
    def __init__(self, dispatcher: Dispatcher, bot: Bot, webhook_url: str, webhook_path: str,handle_in_background: bool = False, **data: Any) -> None:
        super().__init__(dispatcher, handle_in_background, **data)
        self.bot = bot
        self.WEBHOOK_URL = webhook_url
        self.router = APIRouter()
        self.webhook_path = webhook_path

        self.dispatcher.startup.register(self.on_startup)
        self.router.add_event_handler(event_type="shutdown", func=self._handle_close)
        self.router.add_api_route(path=self.webhook_path, endpoint=self.handle, methods=["POST"])

        
        workflow_data = {
            "router": self.router,
            "dispatcher": self.dispatcher,
            **self.dispatcher.workflow_data,
        }

        async def on_startup() -> None:  # pragma: no cover
            await self.dispatcher.emit_startup(**workflow_data)

        async def on_shutdown() -> None:  # pragma: no cover
            await self.dispatcher.emit_shutdown(**workflow_data)

        self.router.add_event_handler("startup", on_startup)
        self.router.add_event_handler("shutdown", on_shutdown)
    
    def get_router(self):
        return self.router

    async def on_startup(self):
        logging.warn("Bot startup event")
        await self.bot.set_webhook(self.WEBHOOK_URL)

    async def _handle_close(self):
        self.close()
    async def close(self):
        logging.info('Bot shutdown event')
        # await dp.storage.close()
        # await dp.storage.wait_closed()
        await self.bot.session.close()
    
    async def resolve_bot(self, request: Request) -> Bot:
        return self.bot
    
    def verify_secret(self, telegram_secret_token: str, bot: Bot) -> bool:
        return super().verify_secret(telegram_secret_token, bot)
    
    async def _background_feed_update(self, bot: Bot, update: Dict[str, Any]) -> None:
        result = await self.dispatcher.feed_raw_update(bot=bot, update=update, **self.data)
        if isinstance(result, TelegramMethod):
            await self.dispatcher.silent_call_request(bot=bot, result=result)
    
    async def _handle_request_background(self, bot: Bot, request: Request) -> Response:
        background_tasks = BackgroundTasks()
        background_tasks.add_task(
            self._background_feed_update, bot=bot, update=await request.json()
        )
        return JSONResponse(content={})
    
    async def _handle_request(self, bot: Bot, request: Request) -> Response:
        result: Optional[TelegramMethod[Any]] = await self.dispatcher.feed_webhook_update(
            bot,
            await request.json(),
            **self.data,
        )
        # r = self._build_response_writer(bot=bot, result=result)
        logging.warn(result)
        return JSONResponse(content=result)
    
    async def handle(self, request: Request):
        bot = await self.resolve_bot(request)
        if self.handle_in_background:
            return await self._handle_request_background(bot=bot, request=request)
        return await self._handle_request(bot=bot, request=request)