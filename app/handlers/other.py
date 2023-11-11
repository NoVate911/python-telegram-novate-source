from aiogram import Router
from aiogram.types import Message

from app.database.requests.select import channel_all_channel_name_by_need_subscribed as select_channel_all_channel_name_by_need_subscribed
from app.misc.filters import IsRegistered, NotRegistered, IsSubscribedToChannels, NotSubscribedToChannels
from app.misc.keyboards import main as main_kb
from app.misc.translations import translations, user_language as get_user_language


router: Router = Router()


@router.message(NotSubscribedToChannels())
async def cmd_need_subscribed_to_channels(msg: Message) -> None:
    user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    need_subscribed_to_channels_dict: str = []
    for need_subscribed_to_channel in await select_channel_all_channel_name_by_need_subscribed(need_subscribed=True):
        channel = await msg.bot.get_chat(chat_id=f'@{need_subscribed_to_channel}')
        need_subscribed_to_channels_dict.append(f"<a href='https://t.me/{need_subscribed_to_channel}'>{channel.title}</a>\n")
    all_need_subscribed_to_channels: str = "".join(need_subscribed_to_channels_dict)
    await msg.reply(text=str.format(translations[user_language]['messages']['need_subscribed_to_channels'], all_need_subscribed_to_channels))

@router.message(IsSubscribedToChannels(), NotRegistered())
async def cmd_need_registered(msg: Message) -> None:
    user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    await msg.reply(text=translations[user_language]['messages']['need_registered'])

@router.message(IsSubscribedToChannels(), IsRegistered())
async def cmd_unknown(msg: Message) -> None:
    user_language: str = await get_user_language(telegram_id=msg.from_user.id, language_code=msg.from_user.language_code)
    await msg.reply(text=translations[user_language]['messages']['unknown'], reply_markup=await main_kb(msg=msg))