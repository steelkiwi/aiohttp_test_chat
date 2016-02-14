import asyncio
import aiohttp_jinja2
from aiohttp import web
from auth.models import User


class Login(web.View):
    @aiohttp_jinja2.template('auth/index.html')
    async def get(self):
        return {'conten': 'You need to login my friend'}

    async def post(self):
        print(self.request, dir(self.request))
        user = User(self.request.db)
        result = user.create_user(self.request['POST'])
        return web.response(result)
