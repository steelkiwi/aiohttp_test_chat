from datetime import datetime
from settings import MESSAGE_COLLECTION


class Message():

    def __init__(self, db, **kwargs):
        print(db, MESSAGE_COLLECTION)
        self.collection = db[MESSAGE_COLLECTION]

    async def save(self, **kw):
        user = kw.get('user')
        msg = kw.get('msg')
        result = await self.collection.insert({'user': user, 'msg': msg, 'time': datetime.now()})
        return result

    async def get_messages(self):
        print(self.collection)
        messages = await self.collection.find({})
        print(messages)
        return messages
