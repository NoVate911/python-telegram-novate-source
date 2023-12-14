import logging

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter, Command

from app.database.requests.insert import channel_by_channel_name as insert_channel_by_channel_name
from app.database.requests.select import channel_by_channel_name as select_channel_by_channel_name, channel_need_subscribed_by_channel_name as select_channel_need_subscribed_by_channel_name, channel_all_channel_name as select_channel_all_channel_name
from app.database.requests.delete import channel_by_channel_name as delete_channel_by_channel_name
from app.database.requests.update import channel_need_subscribed_by_channel_name as update_channel_need_subscribed_by_channel_name
from app.misc.filters import IsSubscribedToChannels, IsRegistered, IsAdministrator
from app.misc.keyboards import main as main_kb, channel as channel_kb
from app.misc.states import ChannelStates
from app.misc.translations import languages, translations, user_language as get_user_language


router: Router = Router()


@router.message(StateFilter(ChannelStates.ADD_INSERT_TELEGRAM_ID, ChannelStates.REMOVE_INSERT_TELEGRAM_ID, ChannelStates.CHANGE_NEED_SUBSCRIBED_INSERT_TELEGRAM_ID), Command(commands=['cancel']))
async def cmd_channel_cancel(msg: Message, state: FSMContext) -> None:
    user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    await state.set_state(ChannelStates.MAIN)
    await msg.reply(text=translations[user_language]['messages']['admin']['channel']['cancel'], reply_markup=await channel_kb(msg=msg))

for language in languages:
    @router.message(StateFilter(None), IsSubscribedToChannels(), IsRegistered(), IsAdministrator(), F.text.lower() == translations[language]['keyboards']['reply']['admin']['channel']['main'].lower())
    async def cmd_channel(msg: Message, state: FSMContext) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        await state.set_state(state=ChannelStates.MAIN)
        await msg.reply(text=translations[user_language]['messages']['admin']['channel']['main'], reply_markup=await channel_kb(msg=msg))

for language in languages:
    @router.message(StateFilter(ChannelStates.MAIN), IsAdministrator(), F.text.lower() == translations[language]['keyboards']['reply']['admin']['channel']['add'].lower())
    async def cmd_channel_add_insert_channel_name(msg: Message, state: FSMContext) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        await state.set_state(state=ChannelStates.ADD_INSERT_TELEGRAM_ID)
        await msg.reply(text=translations[user_language]['messages']['admin']['channel']['add']['channel_name'], reply_markup=ReplyKeyboardRemove())

@router.message(StateFilter(ChannelStates.ADD_INSERT_TELEGRAM_ID), IsAdministrator())
async def cmd_channel_add(msg: Message, state: FSMContext) -> None:
    user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    max_length: int = 32
    if len(msg.text) <= max_length:
        try:
            channel = await msg.bot.get_chat(chat_id=f'@{msg.text}')
            if channel.type == 'channel':
                channel_member = await msg.bot.get_chat_member(chat_id=f'@{msg.text}', user_id=msg.from_user.id)
                if channel_member.status != 'left':
                    if not await select_channel_by_channel_name(channel_name=msg.text):
                        if await insert_channel_by_channel_name(channel_name=msg.text):
                            await state.set_state(state=ChannelStates.MAIN)
                            await msg.reply(text=str.format(translations[user_language]['messages']['admin']['channel']['add']['success'], msg.text), reply_markup=await channel_kb(msg=msg))
                            return
        except Exception as ex:
            logging.error(ex)
    await msg.reply(text=translations[user_language]['messages']['admin']['channel']['add']['channel_name_error'])
    await msg.answer(text=translations[user_language]['messages']['admin']['channel']['add']['channel_name'])

for language in languages:
    @router.message(StateFilter(ChannelStates.MAIN), IsAdministrator(), F.text.lower() == translations[language]['keyboards']['reply']['admin']['channel']['remove'].lower())
    async def cmd_channel_remove_insert_channel_name(msg: Message, state: FSMContext) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        await state.set_state(state=ChannelStates.REMOVE_INSERT_TELEGRAM_ID)
        await msg.reply(text=translations[user_language]['messages']['admin']['channel']['remove']['channel_name'], reply_markup=ReplyKeyboardRemove())

@router.message(StateFilter(ChannelStates.REMOVE_INSERT_TELEGRAM_ID), IsAdministrator())
async def cmd_channel_remove(msg: Message, state: FSMContext) -> None:
    user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    max_length: int = 32
    if len(msg.text) <= max_length:
        try:
            channel = await msg.bot.get_chat(chat_id=f'@{msg.text}')
            if channel.type == 'channel':
                channel_member = await msg.bot.get_chat_member(chat_id=f'@{msg.text}', user_id=msg.from_user.id)
                if channel_member.status != 'left':
                    if await select_channel_by_channel_name(channel_name=msg.text):
                        if await delete_channel_by_channel_name(channel_name=msg.text):
                            await state.set_state(state=ChannelStates.MAIN)
                            await msg.reply(text=str.format(translations[user_language]['messages']['admin']['channel']['remove']['success'], msg.text), reply_markup=await channel_kb(msg=msg))
                            return
        except Exception as ex:
            logging.error(ex)
    await msg.reply(text=translations[user_language]['messages']['admin']['channel']['remove']['channel_name_error'])
    await msg.answer(text=translations[user_language]['messages']['admin']['channel']['remove']['channel_name'])

for language in languages:
    @router.message(StateFilter(ChannelStates.MAIN), IsAdministrator(), F.text.lower() == translations[language]['keyboards']['reply']['admin']['channel']['change_need_subscribed'].lower())
    async def cmd_channel_change_need_subscribed_insert_channel_name(msg: Message, state: FSMContext) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        await state.set_state(state=ChannelStates.CHANGE_NEED_SUBSCRIBED_INSERT_TELEGRAM_ID)
        await msg.reply(text=translations[user_language]['messages']['admin']['channel']['change_need_subscribed']['channel_name'], reply_markup=ReplyKeyboardRemove())

@router.message(StateFilter(ChannelStates.CHANGE_NEED_SUBSCRIBED_INSERT_TELEGRAM_ID), IsAdministrator())
async def cmd_channel_change_need_subscribed(msg: Message, state: FSMContext) -> None:
    user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    max_length: int = 32
    if len(msg.text) <= max_length:
        try:
            channel = await msg.bot.get_chat(chat_id=f'@{msg.text}')
            if channel.type == 'channel':
                channel_member = await msg.bot.get_chat_member(chat_id=f'@{msg.text}', user_id=msg.from_user.id)
                if channel_member.status != 'left':
                    if await select_channel_by_channel_name(channel_name=msg.text):
                        if await update_channel_need_subscribed_by_channel_name(channel_name=msg.text, need_subscribed=True if not await select_channel_need_subscribed_by_channel_name(channel_name=msg.text) else False):
                            await state.set_state(state=ChannelStates.MAIN)
                            await msg.reply(text=str.format(translations[user_language]['messages']['admin']['channel']['change_need_subscribed']['success'], msg.text, 'обязательную' if await select_channel_need_subscribed_by_channel_name(channel_name=msg.text) else 'не обязательную'), reply_markup=await channel_kb(msg=msg))
                            return
        except Exception as ex:
            logging.error(ex)
    await msg.reply(text=translations[user_language]['messages']['admin']['channel']['change_need_subscribed']['channel_name_error'])
    await msg.answer(text=translations[user_language]['messages']['admin']['channel']['change_need_subscribed']['channel_name'])

for language in languages:
    @router.message(StateFilter(ChannelStates.MAIN), IsAdministrator(), F.text.lower() == translations[language]['keyboards']['reply']['admin']['channel']['list'].lower())
    async def cmd_channel_list(msg: Message) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        channel_all_channel_name: list[tuple[str]] = await select_channel_all_channel_name()
        channel_all_dict: str = []
        for channel_name in channel_all_channel_name:
            channel = await msg.bot.get_chat(chat_id=f'@{channel_name}')
            channel_all_dict.append(f"[{'+' if await select_channel_need_subscribed_by_channel_name(channel_name=channel_name) else '-'}] <a href='https://t.me/{channel_name}'>{channel.title}</a>\n")
        all_channels: str = "".join(channel_all_dict)
        await msg.reply(text=str.format(translations[user_language]['messages']['admin']['channel']['list'], all_channels), reply_markup=await channel_kb(msg=msg))

for language in languages:
    @router.message(StateFilter(ChannelStates.MAIN), F.text.lower() == translations[language]['keyboards']['reply']['admin']['channel']['back'].lower())
    async def cmd_channel_back(msg: Message, state: FSMContext) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        await state.clear()
        await msg.reply(text=translations[user_language]['messages']['admin']['channel']['back'], reply_markup=await main_kb(msg=msg))