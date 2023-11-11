from sqlalchemy import insert

from app.database.init import async_session
from app.database.models import User


async def user_by_telegram_id(telegram_id: int) -> bool:
    async with async_session() as session:
        try:
            await session.execute(insert(User).values({User.telegram_id: telegram_id}))
            await session.commit()
            return True
        except Exception:
            await session.rollback()
            return False