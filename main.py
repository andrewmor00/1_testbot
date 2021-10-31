import telebot
# from telebot import types

bot = telebot.TeleBot("token")


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



