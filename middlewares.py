import asyncio
from envparse import env
from motor import motor_asyncio as ma

env.read_envfile('.env')


async def db_handler():
    async def factory(app, handler):
        async def middleware(request):
            if request.path.startswith('/static/') or request.path.startswith('/_debugtoolbar'):
                response = await handler(request)
                return response
            
            client = ma.AsyncIOMotorClient(env.str('MONGO_HOST'), env.int('MONGO_PORT'))
            db = client[env.str('MONGO_DB_NAME')]
            db.authenticate(env.str('MONGO_USER'), env.str('MONGO_PASS'))
            request.db = db
            response = await handler(request)
            client.close()
            return response
        return middleware
    return factory
