from chat.views import ChatList
from auth.views import Login, SignIn, SignOut


routes = [
    ('GET', '/',        ChatList,  'main'),
    ('*',   '/login',   Login,     'login'),
    ('*',   '/signin',  SignIn,    'signin'),
    ('*',   '/signout', SignOut,   'signout'),
]
