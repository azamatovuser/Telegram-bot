import logging
from aiogram import Bot, Dispatcher, executor, types

TOKEN_IPI = '5307377653:AAGShTS5T2i-B6XbPkafVVzS1ZjLgBUbEo0'
logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN_IPI)
a = Dispatcher(bot)


@a.message_handler(commands = ['start'])
async def yeah(message: types.Message):
    await message.answer('Yo! you are at home bro, relax')


@a.message_handler(commands = ['help'])
async def letsgo(message: types.Message):
    await message.answer('You wanna problems?')


@a.message_handler()
async def bro(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(a, skip_updates=True)