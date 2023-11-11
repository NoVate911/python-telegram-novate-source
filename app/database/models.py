from sqlalchemy import Integer, BigInteger, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy import String

from config import OWNER_TELEGRAM_ID


class Base(DeclarativeBase, AsyncAttrs):
    pass

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    referral_id: Mapped[int] = mapped_column(BigInteger, nullable=False, default=OWNER_TELEGRAM_ID)
    language_code: Mapped[str] = mapped_column(String(3), nullable=False, default='ru')

class Channel(Base):
    __tablename__ = 'channels'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    channel_name: Mapped[str] = mapped_column(String(32), nullable=False)
    need_subscribed: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)