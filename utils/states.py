from typing import Final
from aiogram.dispatcher.filters.state import StatesGroup, State


class ADPosting(StatesGroup):
    WriteText: Final = State()
    CheckPost: Final = State()
    SendPost: Final = State()


class Register(StatesGroup):
    StartState: Final = State()
    SucceedSub: Final = State()


class Dialog(StatesGroup):
    first_step: Final = State()
    second_step: Final = State()
    third_step: Final = State()
    questions: Final = State()
    make_application_take_name: Final = State()
    take_number: Final = State()
    take_email: Final = State()
    ending: Final = State()

class AddAdmin(StatesGroup):
    TakeUserId: Final = State()

