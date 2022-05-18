import telebot
import logging

#логирование
logging.basicConfig(format='%(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

#указание токена бота
bot = telebot.TeleBot('5352935775:AAENA4YzYLSlHp6jqdfI3mR9wOK89o7aGaw')

#тело приветствия
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  if (message.text).title() == "Аванс":
      bot.send_message(message.from_user.id, "Сейчас рассчитаем твой аванс")
  elif (message.text).title() == "Зарплата":
      bot.send_message(message.from_user.id, "Сейчас рассчитаем твою зарплату")
  elif message.text == '/start':
      bot.send_message(message.from_user.id, "Напиши 'Аванс' или 'Зарплата'")
  elif message.text == "/help":
      bot.send_message(message.from_user.id, "Напиши 'Аванс' или 'Зарплата'")
  else:
      bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

#










#проверка на новые сообщения
bot.polling(none_stop=True, interval=0)

