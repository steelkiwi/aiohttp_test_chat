from blog.views import blog_list
from auth.views import login


routes = [
    ('GET', '/', blog_list),
    ('GET', '/login', login)
]
