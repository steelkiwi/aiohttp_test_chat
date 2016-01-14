import asyncio
import aiohttp_jinja2
from aiohttp import web


@aiohttp_jinja2.template('auth/index.html')
async def login(request):
	return {'content': 'You need to login my friend'}
