import asyncio
from motor import motor_asyncio as ma
from settings import *


def db_handler():
    async def factory(app, handler):
        async def middleware(request):
            print(request.path)
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
    return factory
