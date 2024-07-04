from aiogram.fsm.state import StatesGroup, State


class MyFSMState(StatesGroup):
    state_game = State()