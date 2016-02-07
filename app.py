#! /usr/bin/env python
import asyncio
import aiohttp_jinja2
import aiohttp_debugtoolbar
import jinja2
import sockjs
from aiohttp_session import session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from aiohttp import web

from routes import routes
from chat.views import WebSocket
from envparse import env
from middlewares import db_handler


env.read_envfile('.env')

key = env.str('SECRET_KEY')

async def init(loop):
    app = web.Application(loop=loop, middlewares=[
#         aiohttp_debugtoolbar.middleware, 
            db_handler(),
#         session_middleware(EncryptedCookieStorage(key))
    ])
    handler = app.make_handler()

#     aiohttp_debugtoolbar.setup(app)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
    sockjs.add_endpoint(app, prefix='/ws', handler=WebSocket)
    # route part
    for route in routes:
        app.router.add_route(route[0], route[1], route[2])
    app.router.add_static('/static', 'static', name='static')
    # end route part

    serv_generator = loop.create_server(handler, '127.0.0.1', 8080)
    return serv_generator, handler, app

loop = asyncio.get_event_loop()
serv_generator, handler, app = loop.run_until_complete(init(loop))
serv = loop.run_until_complete(serv_generator)
print('start server', serv.sockets[0].getsockname())
try:
    loop.run_forever()
except KeyboardInterrupt:
    print('Stop server begin')
finally:
    loop.run_until_complete(handler.finish_connections(1.0))
    serv.close()
    loop.run_until_complete(serv.wait_closed())
    loop.run_until_complete(app.finish())
loop.close()
print('Stop server end')
