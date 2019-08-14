# -*- coding: utf-8 -*-
import os
import telebot
# import some_api_lib


# Example of your code beginning
#           Config vars
TG_BOT_TOKEN = os.environ.get["TG_BOT_TOKEN"]
some_api_token = os.environ.get['SOME_API_TOKEN']


#BOT_TOKEN = config.BOT_TOKEN



bot = telebot.TeleBot(TG_BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.polling()
