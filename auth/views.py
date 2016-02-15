from time import time
import aiohttp_jinja2
from aiohttp_session import get_session
from aiohttp import web
from auth.models import User


def redirect_to_main(request):
    url = request.app.router['main'].url()
    raise web.HTTPFound(url)


def set_session(session, result):
    if isinstance(result, int):
        session['user'] = result
        session['last_visit'] = time()
        redirect_to_main()
    return result


class Login(web.View):

    @aiohttp_jinja2.template('auth/login.html')
    async def get(self):
        session = await get_session(self.request)
        if session.get('user'):
            self.redirect_to_main()
        return {'conten': 'You need to login my friend'}

    async def post(self):
        data = await self.request.post()
        user = User(self.request.db, data)
        result = await user.create_user()
        session = await get_session(self.request)
        return web.Response(body=set_session(session, result))


class Sign(web.View):

    @aiohttp_jinja2.template('auth/sign.html')
    async def get(self, **kw):
        return {'conten': 'Please enter login or email'}

    async def post(self, **kw):
        data = await self.request.post()
        user = User(self.request.db, data)
        result = await user.check_user()
        print(result)
        session = await get_session(self.request)
        return web.Response(body=set_session(session, result))
