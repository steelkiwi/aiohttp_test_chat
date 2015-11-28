#! /usr/bin/env python
import asyncio

from aiohttp import web

async def hello(request):
    return web.Response(body=b'Hello world')

app = web.Application()
app.router.add_route('GET', '/', hello)

loop = asyncio.get_event_loop()
handler = app.make_handler()
serv_generator = loop.create_server(handler, '127.0.0.1', 8080)
serv = loop.run_until_complete(serv_generator)
print('start server', serv.sockets[0].getsockname())
try:
    loop.run_forever()
except KeyboardInterrupt:
    print('Stop server')
finally:
    loop.run_until_complete(handler.finish_connections(1.0))
    serv.close()
    loop.run_until_complete(serv.wait_closed())
    loop.run_until_complete(app.finish())
loop.close()
