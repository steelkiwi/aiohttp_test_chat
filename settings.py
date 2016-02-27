from os.path import isfile
from envparse import env


if isfile('.env'):
    env.read_envfile('.env')

DEBUG = env.bool('DEBUG', default=False)

SITE_HOST = env.str('HOST')
SITE_PORT = env.int('PORT')
SECRET_KEY = env.str('SECRET_KEY')
MONGO_HOST = env.str('MONGO_HOST')
MONGO_PORT = env.int('MONGO_PORT')
MONGO_DB_NAME = env.str('MONGO_DB_NAME')
MONGO_USER = env.str('MONGO_USER')
MONGO_PASS = env.str('MONGO_PASS')

MESSAGE_COLLECTION = 'messages'
USER_COLLECTION = 'users'
