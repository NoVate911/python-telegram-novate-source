from typing import Final

from aiogram.fsm.state import State, StatesGroup


class HelpStates(StatesGroup):
    MAIN: Final = State()