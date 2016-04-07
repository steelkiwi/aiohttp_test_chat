## Python aiohttp - testing with a simple chat

This repo contains examples from article in [our blog](http://steelkiwi.com/blog/an-example-of-a-simple-chat-written-in-aiohttp/).

For creating this chat I used aiohttp -
 asynchronous web framework, written by python core developers.

Also I used Mongodb with motor(asyncronous driver) as database, jinja2 for templates,
envparse for working with secure environment variables

For beginning you can install requirements to virtualenv

```python
pip install -r requirements.txt
```

You must add config *.env* file there will be your secure settings( database connection, secret salt etc.)

Short sample *.env* file

```
DEBUG='False'
MONGO_HOST='mongodb://user:pass@mongo_host:mongo_port/mongo_database'
MONGO_DB_NAME='mongo_database'
SECRET_KEY='some secure key'
HOST='127.0.0.1'
PORT=8000
```

To run server you need just type to console

```
./app.py
```
