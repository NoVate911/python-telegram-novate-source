import random

from yoomoney import Quickpay

from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from config import PAYMENTS_SETTINGS
from app.database.requests.insert import donate_by_telegram_id as insert_donate_by_telegram_id
from app.database.requests.select import donate_id_by_identificator as select_donate_id_by_identificator, donate_all_identificator as select_donate_all_identificator, donate_telegram_id_by_identificator as select_donate_telegram_id_by_identificator, donate_status_by_identificator as select_donate_status_by_identificator, donate_sum_by_identificator as select_donate_sum_by_identificator
from app.misc.filters import IsSubscribedToChannels, IsRegistered
from app.misc.keyboards import main as main_kb, donate as donate_kb
from app.misc.states import DonateStates
from app.misc.translations import languages, translations, user_language as get_user_language


router: Router = Router()


for language in languages:
    @router.message(StateFilter(None), IsSubscribedToChannels(), IsRegistered(), F.text.lower() == translations[language]['keyboards']['reply']['user']['donate']['main'].lower())
    async def cmd_donate(msg: Message, state: FSMContext) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        await state.set_state(state=DonateStates.MAIN)
        await msg.reply(text=translations[user_language]['messages']['user']['donate']['main'], reply_markup=await donate_kb(msg=msg))

for language in languages:
    @router.message(StateFilter(DonateStates.MAIN), F.text.lower() == translations[language]['keyboards']['reply']['user']['donate']['get_link'].lower())
    async def cmd_donate_get_link_insert_sum(msg: Message, state: FSMContext) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        await state.set_state(state=DonateStates.INSERT_SUM)
        await msg.reply(text=translations[user_language]['messages']['user']['donate']['get_link']['insert_sum'], reply_markup=ReplyKeyboardRemove())

@router.message(StateFilter(DonateStates.INSERT_SUM))
async def cmd_donate_get_link(msg: Message, state: FSMContext) -> None:
    user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    min_sum: int = 1
    max_sum: int = 999999
    if not msg.text.isdigit() or int(msg.text) < min_sum or int(msg.text) > max_sum:
        await msg.reply(text=str.format(translations[user_language]['messages']['user']['donate']['get_link']['insert_sum_error'], min_sum))
        await msg.answer(text=translations[user_language]['messages']['user']['donate']['get_link']['insert_sum'])
        return
    quickpay: Quickpay = Quickpay(receiver=PAYMENTS_SETTINGS['receiver'], quickpay_form=PAYMENTS_SETTINGS['quickpay_form'], targets=PAYMENTS_SETTINGS['targets'], paymentType=PAYMENTS_SETTINGS['paymentType'], sum=int(msg.text), label=str.format(PAYMENTS_SETTINGS['label'], msg.from_user.id, random.randint(0, 9999), msg.text))
    if await insert_donate_by_telegram_id(identificator=quickpay.label, telegram_id=msg.from_user.id, sum=quickpay.sum):
        await state.set_state(state=DonateStates.MAIN)
        await msg.reply(text=str.format(translations[user_language]['messages']['user']['donate']['get_link']['success'], await select_donate_id_by_identificator(identificator=quickpay.label), quickpay.redirected_url), reply_markup=await donate_kb(msg=msg))

for language in languages:
    @router.message(StateFilter(DonateStates.MAIN), F.text.lower() == translations[language]['keyboards']['reply']['user']['donate']['personal_statistics'].lower())
    async def cmd_donate_personal_statistics(msg: Message) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        donate_all_identificator: list[tuple[str]] = await select_donate_all_identificator()
        donate_sum_awaiting_identification: int = 0
        donate_sum_passed_identification: int = 0
        for donate_identificator in donate_all_identificator:
            if await select_donate_telegram_id_by_identificator(identificator=donate_identificator) == msg.from_user.id:
                if await select_donate_status_by_identificator(identificator=donate_identificator):
                    donate_sum_passed_identification += await select_donate_sum_by_identificator(identificator=donate_identificator)
                else:
                    donate_sum_awaiting_identification += await select_donate_sum_by_identificator(identificator=donate_identificator)
        await msg.reply(text=str.format(translations[user_language]['messages']['user']['donate']['personal_statistics'], donate_sum_passed_identification + donate_sum_awaiting_identification, donate_sum_passed_identification, donate_sum_awaiting_identification), reply_markup=await donate_kb(msg=msg))

for language in languages:
    @router.message(StateFilter(DonateStates.MAIN), F.text.lower() == translations[language]['keyboards']['reply']['user']['donate']['back'].lower())
    async def cmd_donate_back(msg: Message, state: FSMContext) -> None:
        user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
        await state.clear()
        await msg.reply(text=translations[user_language]['messages']['user']['donate']['back'], reply_markup=await main_kb(msg=msg))