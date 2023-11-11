from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter, Command

from config import OWNER_TELEGRAM_ID
from app.database.requests.select import user_by_telegram_id as select_user_by_telegram_id, user_administrator_by_telegram_id as select_user_administrator_by_telegram_id, user_all_telegram_id as select_user_all_telegram_id
from app.database.requests.update import user_administrator_by_telegram_id as update_user_administrator_by_telegram_id
from app.misc.filters import IsSubscribedToChannels, IsRegistered, IsAdministrator
from app.misc.keyboards import main as main_kb
from app.misc.states import AdministratorStates
from app.misc.translations import languages, translations, user_language as get_user_language


router: Router = Router()


@router.message(StateFilter(AdministratorStates.SET_INSERT_TELEGRAM_ID, AdministratorStates.UNSET_INSERT_TELEGRAM_ID), IsSubscribedToChannels(), IsRegistered(), IsAdministrator(), Command(commands=['cancel']))
async def cmd_administrator_cancel(msg: Message, state: FSMContext) -> None:
    user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    await state.clear()
    await msg.reply(text=translations[user_language]['messages']['admin']['administrator']['cancel'], reply_markup=await main_kb(msg=msg))

for language in languages:
    @router.message(StateFilter(None), IsSubscribedToChannels(), IsRegistered(), IsAdministrator(), F.text.lower() == translations[language]['keyboards']['reply']['admin']['administrator']['set'].lower())
    async def cmd_administrator_set_insert_telegram_id(msg: Message, state: FSMContext) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        await state.set_state(state=AdministratorStates.SET_INSERT_TELEGRAM_ID)
        await msg.reply(text=translations[user_language]['messages']['admin']['administrator']['set']['telegram_id'], reply_markup=ReplyKeyboardRemove())

@router.message(StateFilter(AdministratorStates.SET_INSERT_TELEGRAM_ID), IsSubscribedToChannels(), IsRegistered(), IsAdministrator())
async def cmd_administrator_set(msg: Message, state: FSMContext) -> None:
    user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    if not msg.text.isdigit() or int(msg.text) == msg.from_user.id or not await select_user_by_telegram_id(telegram_id=msg.text) or await select_user_administrator_by_telegram_id(telegram_id=msg.text):
        await msg.reply(text=translations[user_language]['messages']['admin']['administrator']['set']['telegram_id_error'])
        await msg.answer(text=translations[user_language]['messages']['admin']['administrator']['set']['telegram_id'])
        return
    if await update_user_administrator_by_telegram_id(telegram_id=msg.text, administrator=True):
        await state.clear()
        user = await msg.bot.get_chat(chat_id=msg.text)
        await msg.reply(text=str.format(translations[user_language]['messages']['admin']['administrator']['set']['success'], user.username, msg.text), reply_markup=await main_kb(msg=msg))

for language in languages:
    @router.message(StateFilter(None), IsSubscribedToChannels(), IsRegistered(), IsAdministrator(), F.text.lower() == translations[language]['keyboards']['reply']['admin']['administrator']['unset'].lower())
    async def cmd_administrator_unset_insert_telegram_id(msg: Message, state: FSMContext) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        await state.set_state(state=AdministratorStates.UNSET_INSERT_TELEGRAM_ID)
        await msg.reply(text=translations[user_language]['messages']['admin']['administrator']['unset']['telegram_id'], reply_markup=ReplyKeyboardRemove())

@router.message(StateFilter(AdministratorStates.UNSET_INSERT_TELEGRAM_ID), IsSubscribedToChannels(), IsRegistered(), IsAdministrator())
async def cmd_administrator_unset(msg: Message, state: FSMContext) -> None:
    user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    if not msg.text.isdigit() or int(msg.text) == msg.from_user.id or int(msg.text) == OWNER_TELEGRAM_ID or not await select_user_by_telegram_id(telegram_id=msg.text) or not await select_user_administrator_by_telegram_id(telegram_id=msg.text):
        await msg.reply(text=translations[user_language]['messages']['admin']['administrator']['unset']['telegram_id_error'])
        await msg.answer(text=translations[user_language]['messages']['admin']['administrator']['unset']['telegram_id'])
        return
    if await update_user_administrator_by_telegram_id(telegram_id=msg.text, administrator=False):
        await state.clear()
        user = await msg.bot.get_chat(chat_id=msg.text)
        await msg.reply(text=str.format(translations[user_language]['messages']['admin']['administrator']['unset']['success'], user.username, msg.text), reply_markup=await main_kb(msg=msg))

for language in languages:
    @router.message(StateFilter(None), IsSubscribedToChannels(), IsRegistered(), IsAdministrator(), F.text.lower() == translations[language]['keyboards']['reply']['admin']['administrator']['list'].lower())
    async def cmd_administrator_list(msg: Message) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        user_all_telegram_id: list[tuple[int]] = await select_user_all_telegram_id()
        user_all_dict: str = []
        for user_telegram_id in user_all_telegram_id:
            if await select_user_administrator_by_telegram_id(telegram_id=user_telegram_id):
                user = await msg.bot.get_chat(chat_id=user_telegram_id)
                user_all_dict.append(f"{'* ' if user_telegram_id == OWNER_TELEGRAM_ID else ''}@{user.username} (<code>{user_telegram_id}</code>)\n")
        user_all: str = "".join(user_all_dict)
        await msg.reply(text=str.format(translations[user_language]['messages']['admin']['administrator']['list'], user_all), reply_markup=await main_kb(msg=msg))