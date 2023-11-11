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
    SET_INSERT_TELEGRAM_ID: Final = State()
    UNSET_INSERT_TELEGRAM_ID: Final = State()