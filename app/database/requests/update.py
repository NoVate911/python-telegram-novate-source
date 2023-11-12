from sqlalchemy import update

from app.database.init import async_session
from app.database.models import User, Channel, Donate


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
        
async def user_administrator_by_telegram_id(telegram_id: int, administrator: bool) -> bool:
    async with async_session() as session:
        try:
            await session.execute(update(User).where(User.telegram_id  == telegram_id).values({User.administrator: administrator}))
            await session.commit()
            return True
        except Exception:
            await session.rollback()
            return False

async def channel_need_subscribed_by_channel_name(channel_name: str, need_subscribed: bool) -> bool:
    async with async_session() as session:
        try:
            await session.execute(update(Channel).where(Channel.channel_name == channel_name).values({Channel.need_subscribed: need_subscribed}))
            await session.commit()
            return True
        except Exception:
            await session.rollback()
            return False
        
async def donate_status_by_identificator(identificator: int, status: bool) -> bool:
    async with async_session() as session:
        try:
            await session.execute(update(Donate).where(Donate.identificator == identificator).values({Donate.status: status}))
            await session.commit()
            return True
        except Exception:
            await session.rollback()
            return False