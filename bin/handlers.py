import asyncio
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
from aiogram import types
from magic_filter import F
from .utils import *
from . import dp, users
from .weather_api_worker import get_data
from .formater import format


@dp.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    await message.answer("Hey, this is your JustAnotherNormal weather bot!")
    await change_loc(message, state)


@dp.message(StateFilter(States.normal), scobochka_filter)
async def mmm(message: types.Message, state: FSMContext):
    await message.answer(')')


@dp.message(StateFilter(States.location_wait), location_filter) 
async def location(message: types.Message, state: FSMContext):
    users[message.from_user.id] = (message.location.latitude, message.location.longitude)
    await state.set_state(States.normal)
    kb = [[types.KeyboardButton(text='Weather'), types.KeyboardButton(text='Change location')]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('Location has been set succesfully!!!', reply_markup=keyboard)


@dp.message(StateFilter(States.location_wait))
async def not_location(message: types.Message):
    await message.answer('This is NOT a location')


@dp.message(F.text=='Weather', StateFilter(States.normal))
@dp.message(Command('weather'), StateFilter(States.normal))
async def get_weather(message: types.Message):
    data = await get_data(users[message.from_user.id][0], users[message.from_user.id][1])
    await message.answer(format(data))


@dp.message(F.text=='Change location', StateFilter(States.normal))
@dp.message(Command('change_location'), StateFilter(States.normal))
async def change_loc(message: types.Message, state:FSMContext):
    kb = [[types.KeyboardButton(text='Send Location', request_location=True)]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer("Can you send your location message, so I can show you your current weather.", reply_markup=keyboard)
    await state.set_state(States.location_wait)


@dp.message(StateFilter(States.normal))
async def stupid_user(message: types.Message):
    await message.answer("I don't understand you!!")
