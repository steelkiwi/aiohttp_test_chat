from chat.views import ChatList
from auth.views import Login


routes = [
    ('GET', '/', ChatList, 'main'),
    ('*', '/login', Login, 'login'),
]
