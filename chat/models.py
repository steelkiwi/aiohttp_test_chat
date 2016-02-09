from settings import MESSAGE_COLLECTION


class Message():

    def __init__(self, *args, **kwargs):
        self.login = kwargs.get('username')
        self.message = kwargs.get('message')

    def save(self, request, **kw):
        collection = request.db.collection(MESSAGE_COLLECTION)
