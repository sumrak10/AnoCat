from typing import Optional, Dict, Any, AsyncGenerator

import ssl
import certifi
from aiohttp.client import ClientSession
from aiohttp.connector import TCPConnector
from aiohttp.http import SERVER_SOFTWARE
from aiohttp.hdrs import USER_AGENT


class URLInputFile:
    def __init__(
        self,
        url: str,
        headers: Optional[Dict[str, Any]] = None,
        timeout: int = 30,
    ):
        """
        Represents object for streaming files from internet

        :param url: URL in internet
        :param headers: HTTP Headers
        :param filename: Filename to be propagated to telegram.
        :param chunk_size: Uploading chunk size
        :param timeout: Timeout for downloading
        """
        if headers is None:
            headers = {}

        self.url = url
        self.headers = headers
        self.timeout = timeout
        self._session = None

    async def read(self, chunk_size: int) -> AsyncGenerator[bytes, None]:
        stream = self.stream_content(
            url=self.url,
            headers=self.headers,
            timeout=self.timeout,
            chunk_size=chunk_size,
            raise_for_status=True,
        )

        async for chunk in stream:
            yield chunk

    async def stream_content(
        self,
        url: str,
        headers: Optional[Dict[str, Any]] = None,
        timeout: int = 30,
        chunk_size: int = 65536,
        raise_for_status: bool = True,
    ) -> AsyncGenerator[bytes, None]:
        if headers is None:
            headers = {}

        session = await self.create_session()

        async with session.get(
            url, timeout=timeout, headers=headers, raise_for_status=raise_for_status
        ) as resp:
            async for chunk in resp.content.iter_chunked(chunk_size):
                yield chunk

    async def create_session(self) -> ClientSession:
        if self._session is None or self._session.closed:
            self._session = ClientSession(
                connector=TCPConnector({
                    "ssl": ssl.create_default_context(cafile=certifi.where()),
                }),
                headers={
                    USER_AGENT: f"{SERVER_SOFTWARE} anocat/file_server/"
                }
            )
        return self._session

