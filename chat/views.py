import asyncio
from datetime import datetime
import aiohttp_jinja2
from aiohttp import web
from chat.models import Message


class ChatList(web.View):
    @aiohttp_jinja2.template('chat/index.html')
    async def get(self):
        print(self.request)
        return {'conten': 'Some contents'}


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
                    message = Message(date=datetime.now(), message=msg.data, user=request.user)
                    print(message.save())
                    wr.send_str(msg.data + 'fggg')
            elif msg.tp == aiohttp.MsgType.error:
                print('socket closed with exception %s' % wr.exception())
        print('Socket connection closed')
        return wr
