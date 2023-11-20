from db.database import async_session
from models.models import User
from sqlalchemy import select


async def create_new_user(username, password):
    async with async_session() as session:
        new_user = User(username=username, hashed_password=password)
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
    return new_user


async def get_user(username):
    async with async_session() as session:
        statement = select(User).where(User.username == username)
        current_user = await session.execute(statement)
        return current_user
