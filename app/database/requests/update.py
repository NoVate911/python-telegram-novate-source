from sqlalchemy import update

from app.database.init import async_session
from app.database.models import User


async def user_language_code_by_telegram_id(telegram_id: int, language_code: str) -> bool:
    async with async_session() as session:
        try:
            await session.execute(update(User).where(User.telegram_id  == telegram_id).values({User.language_code: language_code}))
            await session.commit()
            return True
        except Exception:
            await session.rollback()
            return False
        
async def user_referral_id_by_telegram_id(telegram_id: int, referral_id: int) -> bool:
    async with async_session() as session:
        try:
            await session.execute(update(User).where(User.telegram_id  == telegram_id).values({User.referral_id: referral_id}))
            await session.commit()
            return True
        except Exception:
            await session.rollback()
            return False