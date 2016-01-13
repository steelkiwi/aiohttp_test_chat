#! /usr/bin/env python
import asyncio
import aiohttp_jinja2
import jinja2
from aiohttp import web
from blog.views import blog_list
from auth.views import login


loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
handler = app.make_handler()

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))

# route part
app.router.add_route('GET', '/', blog_list)
app.router.add_route('GET', '/login', login)


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
