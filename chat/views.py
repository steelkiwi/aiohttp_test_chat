import asyncio
import aiohttp_jinja2
from aiohttp import web


class ChatList(web.View):
    @aiohttp_jinja2.template('chat/index.html')
    async def get(self):
        print(self.request)
        return {'content': 'Some contents'}


class WebSocket(web.View):

    async def get(self):
        print('before soc')
        wr = web.WebSocketResponse()
        await wr.prepare(self.request)
        print('Socket connect start')
        print(wr)
        async for msg in wr:
            print(msg)
            if msg.tp == aiohttp.MsgType.text:
                if msg.data == 'close':
                    await wr.close()
                else:
                    wr.send_str(msg.data + 'fggg')
            elif msg.tp == aiohttp.MsgType.error:
                print('socket closed with exception %s' % wr.exception())
        print('Socket connection closed')
        return wr
