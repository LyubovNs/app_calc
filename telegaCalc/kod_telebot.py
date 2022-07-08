# версия рабочая

import telebot
import logging
# import main


#логирование
import config

logging.basicConfig(format='%(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

#указание токена бота
bot = telebot.TeleBot(config.token)

#тело приветствия
@bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#   if (message.text).title() == "Аванс":
#       bot.send_message(message.from_user.id, "Расчет аванса. Введите оклад за месяц с НДС: ")
#       if (message.text).isdigit():
#           bot.send_message(message.from_user.id, "Для какого месяца считаем")
#       else:
#           bot.send_message(message.chat.id, "Введите число")

def start(message):
    if (message.text).title() == "Аванс":
        oklad = bot.send_message(message.chat.id, 'Расчет аванса. Введите оклад за месяц с НДС: ')
        bot.register_next_step_handler(oklad, v_oklad)
    elif (message.text).title() == "Зарплата":
        bot.send_message(message.from_user.id, "Расчет зарплаты.")
    elif message.text == '/start':
        bot.send_message(message.from_user.id, "Напиши 'Аванс' или 'Зарплата'")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'Аванс' или 'Зарплата'")
    else:
      bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

def v_oklad(message):
    bot.send_message(message.chat.id, 'Оклад: \n{}'.format(message.text))


# @bot.message_handler(content_types=['text'])
# def get_text_messages(message):
#     (message.text).title()

#проверка на новые сообщения
bot.polling(none_stop=True, interval=0)

