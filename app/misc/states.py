from typing import Final

from aiogram.fsm.state import State, StatesGroup


class HelpStates(StatesGroup):
    MAIN: Final = State()

class ReferralStates(StatesGroup):
    MAIN: Final = State()

class RequestStates(StatesGroup):
    MAIN: Final = State()
    INSERT_MESSAGE: Final = State()

class AdministratorStates(StatesGroup):
    MAIN: Final = State()
    SET_INSERT_TELEGRAM_ID: Final = State()
    UNSET_INSERT_TELEGRAM_ID: Final = State()

class ChannelStates(StatesGroup):
    MAIN: Final = State()
    ADD_INSERT_TELEGRAM_ID: Final = State()
    REMOVE_INSERT_TELEGRAM_ID: Final = State()
    CHANGE_NEED_SUBSCRIBED_INSERT_TELEGRAM_ID: Final = State()