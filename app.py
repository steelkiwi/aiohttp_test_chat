#! /usr/bin/env python
import asyncio
import aiohttp_jinja2
import jinja2
from aiohttp import web
from routes import routes
from envparse import env
from motor import motor_asyncio as ma


env.read_envfile('.env')
loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
handler = app.make_handler()

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

# route part
for route in routes:
    app.router.add_route(route[0], route[1], route[2])
app.router.add_static('/static', 'static', name='static')

client = ma.AsyncIOMotorClient(env.str('MONGO_HOST'), env.int('MONGO_PORT'))
print(client)

serv_generator = loop.create_server(handler, '127.0.0.1', 8080)
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
