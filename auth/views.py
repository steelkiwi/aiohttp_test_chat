from time import time
import aiohttp_jinja2
from aiohttp_session import get_session
from aiohttp import web
from auth.models import User


def redirect(request, router_name):
    url = request.app.router[router_name].url()
    raise web.HTTPFound(url)


def set_session(session, result, request):
    def session_user(user_id):
        session['user'] = user_id
        session['last_visit'] = time()

    if isinstance(result, int):
        session_user(result)
        redirect(request, 'main')
    elif isinstance(result, dict):
        print(str(result['_id']))
        session_user(str(result['_id']))
        redirect(request, 'main')
    return result


class Login(web.View):

    @aiohttp_jinja2.template('auth/login.html')
    async def get(self):
        session = await get_session(self.request)
        if session.get('user'):
            redirect(self.request, 'main')
        return {'conten': 'Please enter login or email'}

    async def post(self):
        data = await self.request.post()
        user = User(self.request.db, data)
        result = await user.check_user()
        print(result, 'login')
        session = await get_session(self.request)
        resp = set_session(session, result, self.request)
        return web.Response(success=0, message=resp)


class SignIn(web.View):

    @aiohttp_jinja2.template('auth/sign.html')
    async def get(self, **kw):
        session = await get_session(self.request)
        if session.get('user'):
            redirect(self.request, 'main')
        return {'conten': 'Please enter your data'}

    async def post(self, **kw):
        data = await self.request.post()
        user = User(self.request.db, data)
        result = await user.create_user()
        print(result, "sign")
        session = await get_session(self.request)
        return web.Response(success=0, message=set_session(session, result, self.request))


class SignOut(web.View):

    async def get(self, **kw):
        session = await get_session(self.request)
        if session.get('user'):
            del session['user']
            redirect(self.request, 'login')
        else:
            raise web.HTTPForbidden(body=b'Forbidden')
