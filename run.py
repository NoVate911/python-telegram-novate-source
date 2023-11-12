import sys
import logging
import asyncio

from yoomoney import Client

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.enums import ParseMode

from config import TOKEN, PAYMENTS_TOKEN
from app.database.init import init as database_init
from app.database.requests.select import donate_all_identificator as select_donate_all_identificator, donate_status_by_identificator as select_donate_status_by_identificator, user_language_code_by_telegram_id as select_user_language_code_by_telegram_id, donate_telegram_id_by_identificator as select_donate_telegram_id_by_identificator, donate_id_by_identificator as select_donate_id_by_identificator
from app.database.requests.update import donate_status_by_identificator as update_donate_status_by_identificator
from app.handlers.init import init as handlers_init
from app.misc.translations import translations


async def main() -> None:
    await database_init()

    bot: Bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp: Dispatcher = Dispatcher(storage=MemoryStorage())
    handlers_init(dp=dp)

    scheduler: AsyncIOScheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    scheduler.add_job(checking_donations, trigger='interval', minutes=60, kwargs={'bot': bot})
    scheduler.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

async def checking_donations(bot: Bot) -> None:
    donate_all_identificator: list[tuple[str]] = await select_donate_all_identificator()
    client: Client = Client(token=PAYMENTS_TOKEN)
    for donate_identificator in donate_all_identificator:
        history = client.operation_history(label=donate_identificator)
        for operation in history.operations:
            if operation.status == 'success':
                if not await select_donate_status_by_identificator(identificator=donate_identificator):
                    if await update_donate_status_by_identificator(identificator=donate_identificator, status=True):
                        try:
                            await bot.send_message(chat_id=await select_donate_telegram_id_by_identificator(identificator=donate_identificator), text=str.format(translations[await select_user_language_code_by_telegram_id(telegram_id=await select_donate_telegram_id_by_identificator(identificator=donate_identificator))]['messages']['user']['donate']['transfer_credited'], await select_donate_id_by_identificator(identificator=donate_identificator)))
                        except Exception as ex:
                            logging.error(ex)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Bot stoppped.")