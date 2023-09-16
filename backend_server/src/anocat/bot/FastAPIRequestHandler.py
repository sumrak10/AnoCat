####################################################################################################

import logging
import secrets
from typing import Any, Dict, Optional

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import Response, JSONResponse, StreamingResponse
from fastapi import BackgroundTasks
from aiogram.methods import TelegramMethod
from aiogram.methods.base import TelegramType
from aiogram import Bot, Dispatcher
from aiogram.webhook.aiohttp_server import BaseRequestHandler

from aiohttp import MultipartWriter
from aiogram.types import InputFile


class FastAPIRequestHandler(BaseRequestHandler):
    def __init__(
            self, 
            dispatcher: Dispatcher, 
            bot: Bot, 
            webhook_url: str, 
            webhook_path: str,
            handle_in_background: bool = False, 
            **data: Any
        ) -> None:
        """
        Handle in background don't work now 
        """
        super().__init__(dispatcher, handle_in_background, **data)
        self.bot = bot
        self.WEBHOOK_URL = webhook_url
        self.router = APIRouter()
        self.webhook_path = webhook_path

        self.dispatcher.startup.register(self.on_startup)
        self.router.add_event_handler(event_type="shutdown", func=self._handle_close)
        self.router.add_api_route(
            path=self.webhook_path, 
            endpoint=self.handle, 
            methods=["POST"]
        )

        
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
    
    async def _background_feed_update(self, bot: Bot, request: Request) -> None:
        # result = await self.dispatcher.feed_raw_update(
        #     bot=bot,
        #     update=update, 
        #      **self.data
        # )
        result = await self.dispatcher.feed_webhook_update(
            bot,
            await request.json(),
            **self.data
        )
        if isinstance(result, TelegramMethod):
            await self.dispatcher.silent_call_request(bot=bot, result=result)
    
    async def _handle_request_background(self, 
        bot: Bot, 
        request: Request, 
        background_tasks: BackgroundTasks
    ) -> Response:
        background_tasks.add_task(
            self._background_feed_update,
            bot=bot,
            request=request
        )
        return JSONResponse(content={})
    
    def _build_response_writer(
        self, bot: Bot, result: Optional[TelegramMethod[TelegramType]]
    ) -> MultipartWriter:
        writer = MultipartWriter(
            "form-data",
            boundary=f"webhookBoundary{secrets.token_urlsafe(16)}",
        )
        if not result:
            return writer

        payload = writer.append(result.__api_method__)
        payload.set_content_disposition("form-data", name="method")

        files: Dict[str, InputFile] = {}
        for key, value in result.model_dump(warnings=False).items():
            value = bot.session.prepare_value(value, bot=bot, files=files)
            if not value:
                continue
            payload = writer.append(value)
            payload.set_content_disposition("form-data", name=key)

        for key, value in files.items():
            payload = writer.append(value.read(bot))
            payload.set_content_disposition(
                "form-data",
                name=key,
                filename=value.filename or key,
            )

        return writer

    async def _handle_request(self, bot: Bot, request: Request) -> Response:
        result = await self.dispatcher.feed_webhook_update(
            bot,
            await request.json(),
            **self.data,
        )
        r = self._build_response_writer(bot=bot, result=result)
        return StreamingResponse(content=iter(r), media_type="form-data")
    
    async def handle(self, request: Request, background_tasks: BackgroundTasks) -> None:
        """
        Handle telegram updates
        """
        bot = await self.resolve_bot(request)
        if self.handle_in_background:
            return await self._handle_request_background(
                bot=bot, 
                request=request, 
                background_tasks=background_tasks
            )
        return await self._handle_request(bot=bot, request=request)