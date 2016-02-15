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
        response = await handler(request)
        client.close()
        return response
    return middleware


async def authorize(app, handler):
    async def middleware(request):
        session = await get_session(request)
        if session.get("user"):
            return await handler(request)
        elif not request.path.startswith('/sign') and not request.path.startswith('/static/'):
            url = request.app.router['sign'].url()
            raise web.HTTPFound(url)
        else:
            return await handler(request)

    return middleware
