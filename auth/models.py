import asyncio
from settings import USER_COLLECTION


class User():
    
    email = None
    login = None
    password = None
    
    def __init__(self, db):
        self.db = db
        self.collection = self.db[USER_COLLECTION]

    async def create_user(self, data, **kw):
        
        self.email = data.get('email')
        self.login = data.get('login')
        self.password = data.get('password')
        user = await self.collection.find_one({'email': self.email})
        if not user:
            result = await self.collection.insert({'email': self.email, 'login': self.login, 'password': self.password})
            print(result)
        else:
            result = b'User exists'
        return result

