import asyncio
from aiohttp import web
from motor import motor_asyncio as ma
from settings import *


async def db_handler(app, handler):
    async def middleware(request):
        print(request.path, handler, type(handler))
        if request.path.startswith('/static/') or request.path.startswith('/_debugtoolbar'):
            response = await handler(request)
            return response

        client = ma.AsyncIOMotorClient(MONGO_HOST, MONGO_PORT)
        db = client[MONGO_DB_NAME]
        db.authenticate(MONGO_USER, MONGO_PASS)
        print(db, 'db', type(handler))
        request.db = db
        response = await handler(request)
        client.close()
        return response
    return middleware


async def authorize(app, handler):
    async def middleware(request):
        if request.get("user"):
            return await handler(request)
        elif not request.path.startswith('/login'):
            print(request.app.router.named_resources(), 'erouter')
            url = request.app.router['login'].url()
            return web.HTTPFound(url)

    return middleware
