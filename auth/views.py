import asyncio
import aiohttp_jinja2
from aiohttp import web


class Login(web.View):
    @aiohttp_jinja2.template('auth/index.html')
    async def get(self):
        print(self.request)
        return {'conten': 'You need to login my friend'}

    async def post(self):
        print(self.request)
        return await web.response(b'post request')
