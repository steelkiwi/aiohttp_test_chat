import asyncio
import sqlalchemy as sa

metadata = sa.MetaData()

tbl = sa.Table('users', metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('username', sa.String(255)),
    sa.Column('email', sa.String(255)),
    sa.Column('password', sa.String(255)),
)


async def create_user_table(engine):
    await metadata.create_all(engine)
