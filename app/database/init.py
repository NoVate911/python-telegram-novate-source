from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from config import DEBUGGING
from app.database.models import Base


engine = create_async_engine(url='sqlite+aiosqlite:///database.sqlite3', echo=DEBUGGING)
async_session = async_sessionmaker(engine)


async def init() -> None:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)