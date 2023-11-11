from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from app.database.init import async_session
from app.database.models import User, Channel


async def user_by_telegram_id(telegram_id: int) -> User | None:
    async with async_session() as session:
        try:
            result: User = await session.execute(select(User).where(User.telegram_id == telegram_id))
            return result.scalars().first()
        except NoResultFound:
            return None
        
async def user_language_code_by_telegram_id(telegram_id: int) -> str | None:
    async with async_session() as session:
        try:
            result: str = await session.execute(select(User.language_code).where(User.telegram_id == telegram_id))
            return result.scalars().first()
        except NoResultFound:
            return None
        
async def channel_all_channel_name_by_need_subscribed(need_subscribed: bool) -> str | None:
    async with async_session() as session:
        try:
            result: str = await session.execute(select(Channel.channel_name).where(Channel.need_subscribed == need_subscribed))
            return result.scalars().all()
        except NoResultFound:
            return None