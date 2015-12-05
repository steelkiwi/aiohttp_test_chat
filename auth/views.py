import asyncio
from aiohttp import web

async def login(request):
    return web.Response(body=b'You need to login')
