from datetime import datetime
from settings import MESSAGE_COLLECTION


class Message():

    def __init__(self, db, **kwargs):
        print(db, MESSAGE_COLLECTION)
        self.collection = db[MESSAGE_COLLECTION]

    async def save(self, user, msg, **kw):
        result = await self.collection.insert({'user': user, 'msg': msg, 'time': datetime.now()})
        return result

    async def get_messages(self):
        print(self.collection, 'start get_messages')
        messages = self.collection.find().sort([('time', 1)])
        return await messages.to_list(length=None)
