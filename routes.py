from chat.views import ChatList
from auth.views import Login, Sign


routes = [
    ('GET', '/',      ChatList, 'main'),
    ('*',   '/login', Login,    'login'),
    ('*',   '/sign',  Sign,     'sign'),
]
