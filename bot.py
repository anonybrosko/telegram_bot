from telebot import TeleBot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

bot = TeleBot("8580606853:AAGj6lRIQ5AAxkVkDafDKfi4aoZ7DyH-Xqc")

@bot.message_handler(commands=['start'])
def start(msg):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="Go to Mine 🪙",
            web_app=WebAppInfo(url="https://afc-coin-miner.netlify.app/")
        )
    )
    bot.send_message(msg.chat.id, "Welcome! Click below to mine:", reply_markup=keyboard)

bot.polling()
