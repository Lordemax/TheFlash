# -*- coding: utf-8 -*-

import telebot

import os

# Example of your code beginning
#           Config vars
TG_BOT_TOKEN = os.environ["TG_BOT_TOKEN"] # working perfectly with this my BOT tken On heruko config vars







bot = telebot.TeleBot(TG_BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
