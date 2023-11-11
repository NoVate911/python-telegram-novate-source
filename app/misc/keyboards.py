from aiogram.types import Message, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from app.misc.translations import translations, user_language as get_user_language


async def main(msg: Message) -> ReplyKeyboardBuilder:
    user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    kb.attach(await user(msg=msg))
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder=translations[user_language]['keyboards']['reply']['title'])

async def user(msg: Message) -> ReplyKeyboardBuilder:
    user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    kb.add(
        KeyboardButton(text=translations[user_language]['keyboards']['reply']['user']['help']['main']),
    )
    return kb

async def admin(msg: Message) -> ReplyKeyboardBuilder:
    user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    return kb

async def help(msg: Message) -> ReplyKeyboardBuilder:
    user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    kb.add(
        KeyboardButton(text=translations[user_language]['keyboards']['reply']['user']['help']['information_bot']),
        KeyboardButton(text=translations[user_language]['keyboards']['reply']['user']['help']['rules_use_bot']),
        KeyboardButton(text=translations[user_language]['keyboards']['reply']['user']['help']['back']),
    )
    kb.adjust(1)
    return kb.as_markup(resize_keyboard=True, input_field_placeholder=translations[user_language]['keyboards']['reply']['title'])