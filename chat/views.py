from datetime import datetime
import aiohttp_jinja2
import sockjs
from aiohttp import web
from chat.models import Message


class ChatList(web.View):
    @aiohttp_jinja2.template('chat/index.html')
    async def get(self):
        return {'conten': 'Some contents'}


async def chat(msg, session):
    if msg.tp == sockjs.MSG_OPEN:
        session.manager.broadcast("Someone joined.")
    elif msg.tp == sockjs.MSG_MESSAGE:
        session.manager.broadcast(msg.data)
    elif msg.tp == sockjs.MSG_CLOSED:
        session.manager.broadcast("Someone left.")
