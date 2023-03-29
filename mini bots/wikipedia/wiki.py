import logging
from aiogram import Bot, Dispatcher, executor, types
import wikipedia

token = '5610496084:AAFmAQcAB1ELDj7vUz55DopNtGufVIBYq6k'
logging.basicConfig(level=logging.INFO)
wikipedia.set_lang('uz')

bot = Bot(token)
a = Dispatcher(bot)


@a.message_handler(commands=['start'])
async def text(message: types.Message):
    await message.reply('Welcome bro!')


@a.message_handler()
async def yap(message: types.Message):
    try:
        b = wikipedia.summary(message.text)
        await message.reply(b)
    except:
        await message.reply('Malumot mavjud emas!')


if __name__ == '__main__':
    executor.start_polling(a, skip_updates='True')