import logging

from aiogram.types import Message
from aiogram.filters import Filter

from app.database.requests.select import user_by_telegram_id as select_user_by_telegram_id, channel_all_channel_name_by_need_subscribed as select_channel_all_channel_name_by_need_subscribed


class IsRegistered(Filter):
    async def __call__(self, msg: Message):
        return True if await select_user_by_telegram_id(telegram_id=msg.from_user.id) else False
    
class IsSubscribedToChannels(Filter):
    async def __call__(self, msg: Message):
        user_subscribed_to_channels: int = 0
        for channel in await select_channel_all_channel_name_by_need_subscribed(need_subscribed=True):
            try:
                user_channel_status = await msg.bot.get_chat_member(chat_id=f'@{channel}', user_id=msg.from_user.id)
                if user_channel_status.status != 'left':
                    user_subscribed_to_channels += 1
            except Exception as ex:
                logging.error(ex)
        return True if user_subscribed_to_channels >= len(await select_channel_all_channel_name_by_need_subscribed(need_subscribed=True)) else False
    
class NotRegistered(Filter):
    async def __call__(self, msg: Message):
        return False if await select_user_by_telegram_id(telegram_id=msg.from_user.id) else True
    
class NotSubscribedToChannels(Filter):
    async def __call__(self, msg: Message):
        user_subscribed_to_channels: int = 0
        for channel in await select_channel_all_channel_name_by_need_subscribed(need_subscribed=True):
            try:
                user_channel_status = await msg.bot.get_chat_member(chat_id=f'@{channel}', user_id=msg.from_user.id)
                if user_channel_status.status != 'left':
                    user_subscribed_to_channels += 1
            except Exception as ex:
                logging.error(ex)
        return False if user_subscribed_to_channels >= len(await select_channel_all_channel_name_by_need_subscribed(need_subscribed=True)) else True