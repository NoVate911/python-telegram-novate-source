import logging

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart, StateFilter

from config import OWNER_TELEGRAM_ID
from app.database.requests.insert import user_by_telegram_id as insert_user_by_telegram_id
from app.database.requests.select import user_by_telegram_id as select_user_by_telegram_id, user_language_code_by_telegram_id as select_user_language_code_by_telegram_id, user_administrator_by_telegram_id as select_user_administrator_by_telegram_id
from app.database.requests.update import user_referral_id_by_telegram_id as update_user_referral_id_by_telegram_id, user_administrator_by_telegram_id as update_user_administrator_by_telegram_id
from app.misc.filters import IsSubscribedToChannels
from app.misc.keyboards import main as main_kb
from app.misc.translations import translations, user_language as get_user_language


router: Router = Router()


@router.message(StateFilter(None), IsSubscribedToChannels(), CommandStart())
async def cmd_start(msg: Message, command: Command = None) -> None:
    user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    if await select_user_by_telegram_id(telegram_id=msg.from_user.id):
        await msg.reply(text=str.format(translations[user_language]['messages']['user']['start']['comeback'], msg.from_user.username), reply_markup=await main_kb(msg=msg))
    else:
        if await insert_user_by_telegram_id(telegram_id=msg.from_user.id):
            await msg.reply(text=str.format(translations[user_language]['messages']['user']['start']['welcome'], msg.from_user.username), reply_markup=await main_kb(msg=msg))
            if command.args:
                if await select_user_by_telegram_id(telegram_id=command.args):
                    if await update_user_referral_id_by_telegram_id(telegram_id=msg.from_user.id, referral_id=command.args):
                        try:
                            user_referrer = await msg.bot.get_chat(chat_id=command.args)
                            await msg.answer(text=str.format(translations[user_language]['messages']['user']['start']['referral_notifications']['for_me'], user_referrer.username), reply_markup=await main_kb(msg=msg))
                            await msg.bot.send_message(chat_id=command.args, text=str.format(translations[await select_user_language_code_by_telegram_id(telegram_id=command.args)]['messages']['user']['start']['referral_notifications']['for_referrer'], msg.from_user.username))
                        except Exception as ex:
                            logging.error(ex)
                else:
                    await msg.answer(text=translations[user_language]['messages']['user']['start']['referral_notifications']['not_found'], reply_markup=await main_kb(msg=msg))
    if int(msg.from_user.id) == OWNER_TELEGRAM_ID:
        if not await select_user_administrator_by_telegram_id(telegram_id=msg.from_user.id):
            if await update_user_administrator_by_telegram_id(telegram_id=msg.from_user.id, administrator=True):
                await msg.answer(text=translations[user_language]['messages']['user']['start']['owner_welcome'], reply_markup=await main_kb(msg=msg))