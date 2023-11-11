from sqlalchemy import select
from sqlalchemy.exc import NoResultFound

from app.database.init import async_session
from app.database.models import User, Channel


async def user_all_telegram_id() -> list[tuple[int]]:
    async with async_session() as session:
        result: list[tuple[int]] = await session.execute(select(User.telegram_id))
        return result.scalars().all()

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

async def user_referral_id_by_telegram_id(telegram_id: int) -> int | None:
    async with async_session() as session:
        try:
            result: int = await session.execute(select(User.referral_id).where(User.telegram_id == telegram_id))
            return result.scalars().first()
        except NoResultFound:
            return None

async def user_all_telegram_id_by_referral_id(referral_id: int) -> list[tuple[int]] | None:
    async with async_session() as session:
        try:
            result: list[tuple[int]] = await session.execute(select(User.telegram_id).where(User.referral_id == referral_id))
            return result.scalars().all()
        except NoResultFound:
            return None
        
async def user_administrator_by_telegram_id(telegram_id: int) -> bool | None:
    async with async_session() as session:
        try:
            result: bool = await session.execute(select(User.administrator).where(User.telegram_id == telegram_id))
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