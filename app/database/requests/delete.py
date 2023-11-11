from sqlalchemy import delete
from sqlalchemy.exc import NoResultFound

from app.database.init import async_session
from app.database.models import Channel


async def channel_by_channel_name(channel_name: str) -> bool:
    async with async_session() as session:
        try:
            await session.execute(delete(Channel).where(Channel.channel_name == channel_name))
            await session.commit()
            return True
        except NoResultFound:
            await session.rollback()
            return False