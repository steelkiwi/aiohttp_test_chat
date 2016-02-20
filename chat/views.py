from datetime import datetime
import aiohttp_jinja2
from aiohttp_session import get_session
from aiohttp import web, MsgType
from auth.models import User
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
                    session = await get_session(self.request)

                    user = User(self.request.db, {'id': session.get('user')})
                    login = await user.get_login()
                    ws.send_str('[%s] (%s) %s\n' % (str(datetime.now().time()), login, msg.data))
            elif msg.tp == MsgType.error:
                print('ws connection closed with exception %s' % ws.exception())

        print('websocket connection closed')

        return ws
