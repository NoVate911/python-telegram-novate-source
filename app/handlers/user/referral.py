from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from aiogram.utils.deep_linking import create_start_link

from app.database.requests.select import user_all_telegram_id_by_referral_id as select_user_all_telegram_id_by_referral_id, user_referral_id_by_telegram_id as select_user_referral_id_by_telegram_id
from app.misc.filters import IsSubscribedToChannels, IsRegistered
from app.misc.keyboards import main as main_kb, referral as referral_kb
from app.misc.states import ReferralStates
from app.misc.translations import languages, translations, user_language as get_user_language


router: Router = Router()


for language in languages:
    @router.message(StateFilter(None), IsSubscribedToChannels(), IsRegistered(), F.text.lower() == translations[language]['keyboards']['reply']['user']['referral']['main'].lower())
    async def cmd_referral(msg: Message, state: FSMContext) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        await state.set_state(state=ReferralStates.MAIN)
        await msg.reply(text=translations[user_language]['messages']['user']['referral']['main'], reply_markup=await referral_kb(msg=msg))

for language in languages:
    @router.message(StateFilter(ReferralStates.MAIN), F.text.lower() == translations[language]['keyboards']['reply']['user']['referral']['personal_statistics'].lower())
    async def cmd_referral_personal_statistics(msg: Message) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        referral_users_telegram_id: list[tuple[int]] = await select_user_all_telegram_id_by_referral_id(referral_id=msg.from_user.id)
        referral_link: str = await create_start_link(bot=msg.bot, payload=str(msg.from_user.id))
        referrer_user = await msg.bot.get_chat(chat_id=await select_user_referral_id_by_telegram_id(telegram_id=msg.from_user.id))
        await msg.reply(text=str.format(translations[user_language]['messages']['user']['referral']['personal_statistics'], len(referral_users_telegram_id), referrer_user.username, referral_link), reply_markup=await referral_kb(msg=msg))

for language in languages:
    @router.message(StateFilter(ReferralStates.MAIN), F.text.lower() == translations[language]['keyboards']['reply']['user']['referral']['back'].lower())
    async def cmd_referral_back(msg: Message, state: FSMContext) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        await state.clear()
        await msg.reply(text=translations[user_language]['messages']['user']['referral']['back'], reply_markup=await main_kb(msg=msg))