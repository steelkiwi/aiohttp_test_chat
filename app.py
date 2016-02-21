#! /usr/bin/env python
import asyncio
import aiohttp_jinja2
import aiohttp_debugtoolbar
import jinja2
from aiohttp_session import session_middleware
from aiohttp_session.cookie_storage import EncryptedCookieStorage
from aiohttp import web

from routes import routes
from middlewares import db_handler, authorize
from settings import *


async def on_shutdown(app):
    for ws in app['websockets']:
        await ws.close(code=1001, message='Server shutdown')


async def shutdown(server, app, handler):

    server.close()
    await server.wait_closed()
    await app.shutdown()
    await handler.finish_connections(10.0)
    await app.cleanup()


async def init(loop):

    app = web.Application(loop=loop, middlewares=[
        session_middleware(EncryptedCookieStorage(SECRET_KEY)),
        authorize,
        db_handler,
#         aiohttp_debugtoolbar.middleware,
    ])
    app['websockets'] = []
    handler = app.make_handler()
    if DEBUG:
        aiohttp_debugtoolbar.setup(app)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

    # route part
    for route in routes:
        app.router.add_route(route[0], route[1], route[2], name=route[3])
    app.router.add_static('/static', 'static', name='static')
    # end route part
    app.on_shutdown.append(on_shutdown)

    serv_generator = loop.create_server(handler, SITE_HOST, SITE_PORT)
    return serv_generator, handler, app

loop = asyncio.get_event_loop()
serv_generator, handler, app = loop.run_until_complete(init(loop))
serv = loop.run_until_complete(serv_generator)
print('start server', serv.sockets[0].getsockname())
try:
    loop.run_forever()
except KeyboardInterrupt:
    print(' Stop server begin')
finally:
    loop.run_until_complete(shutdown(serv, app, handler))
    loop.close()
print('Stop server end')
