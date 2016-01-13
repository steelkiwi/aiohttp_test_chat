import asyncio
import aiohttp_jinja2
from aiohttp import web


@aiohttp_jinja2.template('blog.index.html')
async def blog_list(request):
    return {'content': 'Some contents'}
