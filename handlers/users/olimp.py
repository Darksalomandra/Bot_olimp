from aiogram import types
from loader import dp


@dp.message_handler(text='/olimp')
async def command_olimp(message: types.Message):
    await message.answer("Тут пока ничего нет")
