from aiogram import types
from loader import dp


@dp.message_handler(text='/help')
async def command_help(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}! \n'
                         f'<b>Предметы по которым есть олимпиады</b>: Биология, География, Информатика, Математика, Физика, Химия, Астрономия, ИЗО, Искусство, История, Лингвистика, Литература, ОБЖ, Обществознание, Предпринимательсво, Право, Психология, Робототехника, Русский язык, Технология, Физкультура, Черчение, Экология, Экономика, Ин.языки.\n'
                         f'<b>Классы</b>: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11.\n'
                         f'<b>Типы</b>: Командные, Личные, Дистанционные, Все.')
