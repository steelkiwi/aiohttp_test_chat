from bson.objectid import ObjectId
from settings import USER_COLLECTION


class User():

    def __init__(self, db, data, **kw):
        self.db = db
        self.collection = self.db[USER_COLLECTION]
        self.email = data.get('email')
        self.login = data.get('login')
        self.password = data.get('password')
        self.id = data.get('id')

    async def check_user(self, **kw):
        return await self.collection.find_one({'login': self.login})

    async def get_login(self, **kw):
        user = await self.collection.find_one({'_id': ObjectId(self.id)})
        return user.get('login')

    async def create_user(self, **kw):
        user = await self.check_user()
        if not user:
            result = await self.collection.insert({'email': self.email, 'login': self.login, 'password': self.password})
        else:
            result = 'User exists'
        return result
