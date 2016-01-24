from blog.views import BlogList
from auth.views import Login


routes = [
    ('GET', '/', BlogList),
    ('GET', '/login', Login)
]
