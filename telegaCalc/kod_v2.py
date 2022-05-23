import telebot
from telebot import types
import logging

from telegram import message

import config
from config import token, get_m, month_check, day, get_s, prep

#логирование
logging.basicConfig(format='%(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

#указание токена бота из файла конфига
bot = telebot.TeleBot(config.token)


#тело приветствия

welcome_message = {
    'start':
        u'Здравствуй, персик\n'
        u'Я умею рассчитывать аванс и зарплату, но пока не умею считать отпускные.\n\n'
        u'Давай попробуем?\n'
        u'Выбери, что будем считать: "Аванс" или "Зарплата"',

    'help':
        u'Выбери, что будем считать: "Аванс" или "Зарплата"'
    }

# month_message = {
#     'choose':
#         u'Для какого месяца считаем?\n'
# }


# функция выбора, что считать

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # кнопки
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Аванс')
    markup.row('Зарплата')

    # сообщение пользователю - приветствие
    msg = bot.send_message(message.from_user.id, welcome_message['start'].format(name=message.from_user.id), reply_markup=markup)

    # для связи функци - принимает в себя сообщение из текущей и говорит о том, что оно будет обработано в следующей функции month
    bot.register_next_step_handler(msg, month)


# функция выбора месяца

@bot.message_handler(content_type=['text'])
def month(message):
    # кнопки
    month = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # проверка работы предыдущей функции
    if message.text == 'Аванс' or message.text == 'Зарплата':
        month.row('Январь')
        month.row('Февраль')
        month.row('Март')
        month.row('Апрель')
        month.row('Май')
        month.row('Июнь')
        month.row('Июль')
        month.row('Август')
        month.row('Сентябрь')
        month.row('Октябрь')
        month.row('Ноябрь')
        month.row('Декабрь')
        month.row('Назад')

        #  сообщение пользователю - выбрать месяц
        msg = bot.send_message(message.from_user.id, 'Выберите месяц', reply_markup=month)

        # для связи функци - принимает в себя сообщение из текущей и говорит о том, что оно будет обработано в следующей функции salary, а также записана в record_m
        bot.register_next_step_handler(msg, record_m)

        bot.register_next_step_handler(msg, salary)
    else:
        # если будет отправлено что-то иное - возврат в предыдущее меню
        send_welcome(message)
        return

# запись ответа (месяц)

def record_m():
    global month
    month = message.text


# функция ввода оклада пользователем

@bot.message_handler(content_type=['text'])
def salary(message):
    # кнопки
    salary = types.ReplyKeyboardMarkup(resize_keyboard=True)
    salary.row('Назад')

    # проверка работы предыдущей функции
    if message.text == 'Назад':
        month(message)
        return
    else:
        if message.text == 'Январь' or message.text == 'Февраль' \
            or message.text == 'Март' or message.text == 'Апрель' \
            or message.text == 'Май' or message.text == 'Июнь' or message.text == 'Июль' \
            or message.text == 'Август' \
            or message.text == 'Сентябрь' or message.text == 'Октябрь' \
            or message.text == 'Ноябрь' \
            or message.text == 'Декабрь':
            # сообщение пользователю ввести оклад
            msg = bot.send_message(message.from_user.id, 'Введите оклад за месяц с НДС: ', reply_markup=salary)
            # для связи функци - принимает в себя сообщение из текущей и говорит о том, что оно будет обработано в следующей функции salary и запись в record_s
            bot.register_next_step_handler(msg, record_s)

            bot.register_next_step_handler(msg, prepay)

        else:
            # если будет отправлено что-то иное - возврат в предыдущее меню
            month(message)
            return

# запись ответа (месяц)

def record_s():
    global salary
    salary = message.text


# Расчет аванса

def prepay(message):
    # проверка работы предыдущей функции
    # кнопки
    salary = types.ReplyKeyboardMarkup(resize_keyboard=True)
    salary.row('Назад')

    if message.text == 'Назад':
        salary(message)
        return
    else:
        if message.text.isdigit():
            get_m()
            month_check()
            day()
            get_s()
            prep()

            msg = bot.send_message(message.from_user.id, prep())







        elif message.text == 'Назад':
            salary(message)
        else:
            salary(message)
            return









#проверка на новые сообщения
bot.polling(none_stop=True, interval=0)

