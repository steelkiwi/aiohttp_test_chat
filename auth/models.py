import asyncio
from settings import USER_COLLECTION


class User():
    
    email = None
    login = None
    password = None
    
    def __init__(self, db):
        self.db = db
        self.collection = self.db[USER_COLLECTION]

    async def create_user(self, **kw):
        print(kw)
        self.email = kw.get('email')
        self.login = kw.get('login')
        self.password = kw.get('password')
        user = await self.collection.find_one({'email': self.email})
        if not user:
            result = await self.collection.insert({'email': self.email, 'login': self.login, 'password': self.password})
            print(result)
        else:
            result = b'User exists'
        return result

