import asyncio
import aiohttp_jinja2
from aiohttp import web
from auth.models import User


class Login(web.View):
    @aiohttp_jinja2.template('auth/index.html')
    async def get(self):
        return {'conten': 'You need to login my friend'}

    async def post(self):
        user = User(self.request.db)
        data = await self.request.post()
        print(data)
        result = await user.create_user(data)
        return web.response(result)
