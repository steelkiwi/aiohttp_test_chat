from datetime import datetime
import aiohttp_jinja2
from aiohttp import web, MsgType
from chat.models import Message


class ChatList(web.View):
    @aiohttp_jinja2.template('chat/index.html')
    async def get(self):
        return {'conten': 'Some contents'}


class WebSocket(web.View):
    async def get(self):
        ws = web.WebSocketResponse()
        await ws.prepare(self.request)

        async for msg in ws:
            print(msg)
            if msg.tp == MsgType.text:
                if msg.data == 'close':
                    await ws.close()
                else:
                    ws.send_str(msg.data + '/answer')
            elif msg.tp == MsgType.error:
                print('ws connection closed with exception %s' % ws.exception())

        print('websocket connection closed')

        return ws
