import sys
import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode

from config import TOKEN
from app.database.init import init as database_init
from app.handlers.init import init as handlers_init


async def main() -> None:
    await database_init()

    bot: Bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp: Dispatcher = Dispatcher(storage=MemoryStorage())
    handlers_init(dp=dp)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stoppped.")