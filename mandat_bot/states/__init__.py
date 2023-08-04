from aiogram.dispatcher.filters.state import StatesGroup, State


class StartStates(StatesGroup):
    kanallar = State()
    number = State()
