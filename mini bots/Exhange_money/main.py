from aiogram import Bot, Dispatcher, executor, types
import requests
import json
import logging

from aiogram.types import user

btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn.add("USD-UZS", "RUB-UZS", "EURO-UZS", "CNY-UZS", "WON-UZS", "DINOR-UZS")
logging.basicConfig(level=logging.INFO)

token = '5695389511:AAGo517MYS0u8YA5-NSKOLzxR2YEQSVR_vA'
bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def first(message: types.Message):
    cap = f"Welcome Dear user | This is currency bot"
    rasm = open('IMAGE/exch.jpeg', 'rb')
    await bot.send_photo(message.chat.id, rasm, caption=cap, reply_markup=btn)

@dp.message_handler(content_types=["text"])
async def second(message: types.Message):
    global inputs, outputs, result, cap
    text = message.text
    if text == "USD-UZS":
        inputs = "USD"
        outputs = "UZS"
        cap = "Dollarning So'mdagi qiymati"
    if text == "RUB-UZS":
        inputs = "RUB"
        outputs = "UZS"
        cap = "Rublning So'mdagi qiymati"
    if text == "EURO-UZS":
        inputs = "EUR"
        outputs = "UZS"
        cap = "Euroning So'mdagi qiymati"
    if text == "CNY-UZS":
        inputs = "CNY"
        outputs = "UZS"
        cap = "Xitoy yenasining So'mdagi qiymati"
    if text == "DINOR-UZS":
        inputs = "KWD"
        outputs = "UZS"
        cap = "Dinorning So'mdagi qiymati"
    if text == "WON-UZS":
        inputs = "KRW"
        outputs = "UZS"
        cap = "Wonning So'mdagi qiymati"

    url = "https://v6.exchangerate-api.com/v6/5d3f18bd0729d305e60f295c/latest/" + inputs
    responses = requests.get(url)
    rest = json.loads(responses.text)
    result = rest["conversion_rates"]["UZS"]
    if message.text.isdigit():
        print(int(message.text) * result)
        await bot.send_message(message.chat.id, int(message.text) * (result))

if __name__ == '__main__':
    executor.start_polling(dp)