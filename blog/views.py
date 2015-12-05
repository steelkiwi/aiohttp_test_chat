import asyncio
from aiohttp import web

async def blog_list(request):
    return web.Response(body=b'Blog list')
