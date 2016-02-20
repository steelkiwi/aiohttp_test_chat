import json
from time import time
from bson.objectid import ObjectId
import aiohttp_jinja2
from aiohttp_session import get_session
from aiohttp import web
from auth.models import User


def redirect(request, router_name):
    url = request.app.router[router_name].url()
    raise web.HTTPFound(url)


def set_session(session, user_id, request):
    session['user'] = str(user_id)
    session['last_visit'] = time()
    print(session)
    redirect(request, 'main')


def convert_json(message):
    return json.dumps({'error': message})


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
        if isinstance(result, dict):
            session = await get_session(self.request)
            set_session(session, str(result['_id']), self.request)
        else:
            return web.Response(content_type='application/json', text=convert_json(result))


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
        print(result, type(result), "sign")
        if isinstance(result, ObjectId):
            session = await get_session(self.request)
            set_session(session, str(result), self.request)
        else:
            return web.Response(content_type='application/json', text=convert_json(result))


class SignOut(web.View):

    async def get(self, **kw):
        session = await get_session(self.request)
        if session.get('user'):
            del session['user']
            redirect(self.request, 'login')
        else:
            raise web.HTTPForbidden(body=b'Forbidden')
