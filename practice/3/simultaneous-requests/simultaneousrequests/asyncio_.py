import asyncio
from datetime import datetime

import httpx


async def _get_user(path: str, client: httpx.AsyncClient):
    await client.get(path)


async def _test(paths: list[str]):
    async with httpx.AsyncClient() as client:
        await asyncio.gather(*(_get_user(path, client) for path in paths))


def test_asyncio(paths: list[str]):
    start_time = datetime.now()
    asyncio.run(_test(paths))
    return datetime.now() - start_time
