from telebot import TeleBot
<<<<<<< HEAD
<<<<<<< HEAD
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
=======
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
>>>>>>> b744999 (Persistent Inline Not Working So Removed It)
=======
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
>>>>>>> b744999 (Persistent Inline Not Working So Removed It)

import os

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
bot = TeleBot(TOKEN)

SUPPORT_COFFEE = os.environ.get("SUPPORT_COFFEE")
SUPPORT_PAYPAL = os.environ.get("SUPPORT_PAYPAL")

@bot.message_handler(commands=['start'])
def start(msg):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="Go to Mine 🪙",
            web_app=WebAppInfo(url="https://anonybrosko.github.io/afc-coin-miner-frontend")
        )
    )
    keyboard.add(
        InlineKeyboardButton(
            text="Support The Game ❤️",
            callback_data="Support"
        )
    )
    bot.send_message(msg.chat.id, "Welcome! Click below to mine:", reply_markup=keyboard)

@bot.message_handler(commands=['support'])
def support(msg):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton(
            text="Buy me a coffee ☕",
            url=SUPPORT_COFFEE
        ),
        InlineKeyboardButton(
            text="PayPal 💰",
            url=SUPPORT_PAYPAL
        )
    )
    bot.send_message(
        msg.chat.id,
        "Thank you for supporting AFC Coin Miner! Choose and option below:",
        reply_markup=keyboard
    )

bot.polling()
