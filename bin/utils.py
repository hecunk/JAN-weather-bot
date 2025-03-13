from aiogram.fsm.state import State
from aiogram import types
from aiogram.fsm.state import StatesGroup


class States(StatesGroup):
    normal = State()
    location_wait = State()

def location_filter(message: types.Message):
    return message.content_type == 'location'

def scobochka_filter(message: types.Message):
    return message.text[-1] == ')'