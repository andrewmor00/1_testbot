import telebot
# from telebot import types

bot = telebot.TeleBot("2047443605:AAGazmJWETi1d9YOrBJhZgIGf7SmDSXqcPE")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Привет!!, Введи название формулы     ')


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == 'Дискриминант':
        bot.send_message(
            message, "C**2 = A**2 + B**2"
        )


bot.infinity_polling()



