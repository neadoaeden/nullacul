import asyncio
from aiohttp import web

async def background_task():
    await asyncio.sleep(5)
    print("Background task finished")

app = web.Application()
app.on_startup.append(lambda: asyncio.create_task(background_task()))
