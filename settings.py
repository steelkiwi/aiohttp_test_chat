from envparse import env

env.read_envfile('.env')


SITE_HOST = env.str('SITE_HOST')
SITE_PORT = env.int('SITE_PORT')
SECRET_KEY = env.str('SECRET_KEY')
MONGO_HOST = env.str('MONGO_HOST')
MONGO_PORT = env.int('MONGO_PORT')
MONGO_DB_NAME = env.str('MONGO_DB_NAME')
MONGO_USER = env.str('MONGO_USER')
MONGO_PASS = env.str('MONGO_PASS')
