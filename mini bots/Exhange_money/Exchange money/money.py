import json
import logging
import requests
from aiogram import Bot, Dispatcher, executor, types

btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn.add("USD-UZS", "RUB-UZS", "CNY-UZS")

token = '5677294552:AAF34JwbSg0Gzm58QU08Rif_xBKhIiili-s'
logging.basicConfig(level=logging.INFO)
bot = Bot(token)
a = Dispatcher(bot)


@a.message_handler(commands = ['start'])
async def start(message: types.Message):
    rasm = open('2022-09-15 19.54.22.jpg', 'rb')
    text = f"Welcome to currency bot!"
    await bot.send_photo(message.chat.id, rasm, caption=text, reply_markup=btn)


@a.message_handler(content_types=['text'])
async def reply(message: types.Message):
    global inputs, outputs, result, cap, rasm1
    rasm1 = open('dollar01.jpg', 'rb')
    text = message.text
    if text == 'USD-UZS':
        inputs = 'USD'
        outputs = 'UZS'
        cap = "Natija 👇🏼"
    if text == 'RUB-UZS':
        inputs = 'RUB'
        outputs = 'UZS'
        cap = "Natija 👇🏼"
    if text == 'CNY-UZS':
        inputs = 'CNY'
        outputs = 'UZS'
        cap = "Natija 👇🏼"

    url = 'https://v6.exchangerate-api.com/v6/df9e83fd757a57cb2b27836c/latest/' + inputs
    come = requests.get(url)
    rest = json.loads(come.text)
    result = rest['conversion_rates']['UZS']
    if message.text.isdigit():
        print(int(message.text) * result)
        await bot.send_photo(message.chat.id, rasm1, caption=cap)
        await bot.send_message(message.chat.id, int(message.text) * result)


if __name__ == '__main__':
    executor.start_polling(a, skip_updates=True)