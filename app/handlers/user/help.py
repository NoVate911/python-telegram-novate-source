from aiogram import Router, F
from aiogram.types import Message, User
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from app.misc.filters import IsSubscribedToChannels, IsRegistered
from app.misc.keyboards import main as main_kb, help as help_kb
from app.misc.states import HelpStates
from app.misc.translations import languages, translations, user_language as get_user_language


router: Router = Router()


for language in languages:
    @router.message(StateFilter(None), IsSubscribedToChannels(), IsRegistered(), F.text.lower() == translations[language]['keyboards']['reply']['user']['help']['main'].lower())
    async def cmd_help(msg: Message, state: FSMContext) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        await state.set_state(state=HelpStates.MAIN)
        await msg.reply(text=translations[user_language]['messages']['user']['help']['main'], reply_markup=await help_kb(msg=msg))

for language in languages:
    @router.message(StateFilter(HelpStates.MAIN), F.text.lower() == translations[language]['keyboards']['reply']['user']['help']['information_bot'].lower())
    async def cmd_help_information_bot(msg: Message) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        bot: User = await msg.bot.get_me()
        await msg.reply(text=str.format(translations[user_language]['messages']['user']['help']['information_bot'], bot.username, "novatesource", translations[user_language]['keyboards']['reply']['user']['request']['main']), reply_markup=await help_kb(msg=msg))

for language in languages:
    @router.message(StateFilter(HelpStates.MAIN), F.text.lower() == translations[language]['keyboards']['reply']['user']['help']['rules_use_bot'].lower())
    async def cmd_help_rules_use_bot(msg: Message) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        await msg.reply(text=str.format(translations[user_language]['messages']['user']['help']['rules_use_bot'], translations[user_language]['keyboards']['reply']['user']['request']['main']), reply_markup=await help_kb(msg=msg))

for language in languages:
    @router.message(StateFilter(HelpStates.MAIN), F.text.lower() == translations[language]['keyboards']['reply']['user']['help']['back'].lower())
    async def cmd_help_back(msg: Message, state: FSMContext) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        await state.clear()
        await msg.reply(text=translations[user_language]['messages']['user']['help']['back'], reply_markup=await main_kb(msg=msg))