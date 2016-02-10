from settings import MESSAGE_COLLECTION


class Message():

    def __init__(self, *args, **kwargs):
        self.collection = request.db.collection(MESSAGE_COLLECTION)
        self.document = kwargs

    async def save(self, request, **kw):
        result = await self.collection.insert(self.document)
        return result
