import asyncio
import aiohttp_jinja2
from aiohttp import web


class BlogList(web.View):
    @aiohttp_jinja2.template('blog/index.html')
    async def get(self):
        print(self.request)
        return {'content': 'Some contents'}
