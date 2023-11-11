from sqlalchemy import insert

from app.database.init import async_session
from app.database.models import User, Channel


async def user_by_telegram_id(telegram_id: int) -> bool:
    async with async_session() as session:
        try:
            await session.execute(insert(User).values({User.telegram_id: telegram_id}))
            await session.commit()
            return True
        except Exception:
            await session.rollback()
            return False
        
async def channel_by_channel_name(channel_name: str) -> bool:
    async with async_session() as session:
        try:
            await session.execute(insert(Channel).values({Channel.channel_name: channel_name}))
            await session.commit()
            return True
        except Exception:
            await session.rollback()
            return False