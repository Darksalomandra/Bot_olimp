from aiogram import types
from loader import dp
from parse_olimp import parse_text

subject_search = ([
    'Биология', 'География', 'Информатика', 'Математика', 'Физика', 'Химия', 'Астрономия', 'ИЗО', 'Искусство',
    'История', 'Лингвистика', 'Литература', 'ОБЖ', 'Обществознание', 'Предпринимательсво', 'Право',
    'Психология', 'Робототехника', 'Русский язык', 'Технология', 'Физкультура', 'Черчение', 'Экология',
    'Экономика', 'Ин.языки'
])

class_search = ([
    str(i) for i in range(1, 12)
])

type_search = ([
    'Командные', 'Личные', 'Дистанционные', 'Все'
])


@dp.message_handler(text='/olimp')
async def command_olimp(message: types.Message):
    await message.answer("Введите предмет (список в разделе помощь):")


@dp.message_handler(text=subject_search)
async def answer1(message: types.Message):
    global s
    s = message.text
    await message.answer("Введите класс от 1 до 11:")


@dp.message_handler(text=class_search)
async def command_olimp(message: types.Message):
    global c
    c = message.text
    await message.answer("Введите тип (список в разделе помощь):")


@dp.message_handler(text=type_search)
async def command_olimp(message: types.Message):
    global t
    t = message.text
    f = parse_text(s, c, t)
    await message.answer(f)
