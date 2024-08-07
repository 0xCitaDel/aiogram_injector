from aiogram.fsm.state import StatesGroup, State


class MainSG(StatesGroup):
    start = State()
    input_code = State()
    get_document = State()
