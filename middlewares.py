from aiohttp import web
from aiohttp_session import get_session
from motor import motor_asyncio as ma
from settings import *


async def db_handler(app, handler):
    async def middleware(request):
        if request.path.startswith('/static/') or request.path.startswith('/_debugtoolbar'):
            response = await handler(request)
            return response

        client = ma.AsyncIOMotorClient(MONGO_HOST, MONGO_PORT)
        db = client[MONGO_DB_NAME]
        db.authenticate(MONGO_USER, MONGO_PASS)
        request.db = db
        if request.path.startswith('/ws/'):
            import ipdb; ipdb.set_trace() # BREAKPOINT
            print(type(handler(request)))
            return handler(request)
        response = await handler(request)
        client.close()
        return response
    return middleware


async def authorize(app, handler):
    async def middleware(request):
        def check_path(path):
            result = True
            for r in ['/login', '/static/', '/signin', '/signout', '/_debugtoolbar/']:
                if path.startswith(r):
                    result = False
            return result

        session = await get_session(request)
        if session.get("user"):
            return await handler(request)
        elif check_path(request.path):
            url = request.app.router['login'].url()
            raise web.HTTPFound(url)
            return handler(request)
        else:
            return await handler(request)

    return middleware
