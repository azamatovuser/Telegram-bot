import logging
from aiogram import Bot, Dispatcher, executor, types
import requests

button = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
button.add("Small hot-dog 🍗", "Medium hot-dog 🌭", "Big hot-dog 🍟", "Huge hot-dog 🧀")

token = '5500917539:AAFXzdFsuj_uGBGYwgsETo06lJyi7id8Ysg'
logging.basicConfig(level=logging.INFO)

bot = Bot(token)
connector = Dispatcher(bot)


@connector.message_handler(commands=['start'])
async def start(message:types.Message):
    await message.reply('Welcome to HotDog!\nWhat would you like to know?', reply_markup=button)


@connector.message_handler(commands=['help'])
async def help(message:types.Message):
    await message.reply('Describe your problem 👇')


@connector.message_handler(content_types=['text'])
async def main(message:types.Message):
    global rasm, words
    text = message.text
    if text == 'Small hot-dog 🍗':
        rasm = open('pict/4137-500617-1.jpg', 'rb')
        words = 'Small hot-dog 🍗\n' '\nHot dog is a food consisting of a grilled or steamed sausage served in the slit of a partially sliced bun\n' '\nPrice: 5$'
    if text == 'Medium hot-dog 🌭':
        rasm = open('pict/1*azFAHEZnlwylmcXHrnF6XQ.jpeg', 'rb')
        words = 'Medium hot-dog 🌭\n' '\nThese types of sausages were culturally imported from Germany and became popular in the United States. It became a working-class street food in the U.S., sold at stands and carts\n' '\nPrice: 10$'
    if text == 'Big hot-dog 🍟':
        rasm = open('pict/443_444_Big_Dogs_Wieners_Jan2019.jpg', 'rb')
        words = 'Big hot-dog 🍟\n' '\nThe hot dog became closely associated with baseball and American culture. Although particularly connected with New York City and its cuisine, the hot dog eventually became ubiquitous throughout the US\n' '\nPrice: 15$'
    if text == 'Huge hot-dog 🧀':
        rasm = open('pict/charred-hot-dogs-with-spicy-mayonnaise-106466-1.jpeg', 'rb')
        words = 'Huge hot-dog 🧀\n' '\nAccording to one story, the use of the complete phrase hot dog in reference to sausage was coined by the newspaper cartoonist\n' '\nPrice: 20$'
    await bot.send_photo(message.chat.id, rasm, caption=words)


if __name__ == '__main__':
    executor.start_polling(connector, skip_updates=True)