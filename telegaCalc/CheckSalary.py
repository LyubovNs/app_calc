# рабочий код на две кнопки

import telebot
from telebot import types
import logging
import datetime
import config

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

    # для связи функци - принимает в себя сообщение из текущей и говорит о том, что оно будет обработано в следующей функции monthes
    bot.register_next_step_handler(msg, monthes)


# функция выбора месяца

@bot.message_handler(content_type=['text'])
def monthes(message):
    # кнопки
    m = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # проверка работы предыдущей функции
    if message.text == 'Аванс' or message.text == 'Зарплата':
        m.row('Январь')
        m.row('Февраль')
        m.row('Март')
        m.row('Апрель')
        m.row('Май')
        m.row('Июнь')
        m.row('Июль')
        m.row('Август')
        m.row('Сентябрь')
        m.row('Октябрь')
        m.row('Ноябрь')
        m.row('Декабрь')
        m.row('Назад')

        #  сообщение пользователю - выбрать месяц
        msg = bot.send_message(message.from_user.id, 'Выберите месяц', reply_markup=m)

        # для связи функци - принимает в себя сообщение из текущей и говорит о том, что оно будет обработано в следующей функции salary, а также записана в record_m
        bot.register_next_step_handler(msg, record_m)

        bot.register_next_step_handler(msg, salary)
    else:
        # если будет отправлено что-то иное - возврат в предыдущее меню
        send_welcome(message)
        return


# запись ответа (месяц)

def record_m(message):
    global month_u
    month_u = message.text

    month_check()


# нумерация месяцов

def month_check():
     global month
     if month_u == 'Январь':
         month = 1
     elif month_u == 'Февраль':
         month = 2
     elif month_u == 'Март':
         month = 3
     elif month_u == 'Апрель':
         month = 4
     elif month_u == 'Май':
         month = 5
     elif month_u == 'Июнь':
         month = 6
     elif month_u == 'Июль':
         month = 7
     elif month_u == 'Август':
         month = 8
     elif month_u == 'Сентябрь':
         month = 9
     elif month_u == 'Октябрь':
         month = 10
     elif month_u == 'Ноябрь':
         month = 11
     elif month_u == 'Декабрь':
         month = 12

     return month


# функция ввода оклада пользователем

@bot.message_handler(content_type=['text'])
def salary(message):
    # кнопки
    # salary = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # salary.row('Назад')

    # проверка работы предыдущей функции
    if message.text == 'Назад':
        monthes(message)
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
            msg = bot.send_message(message.from_user.id, 'Введите оклад за месяц с НДС: ')
            # для связи функци - принимает в себя сообщение из текущей и говорит о том, что оно будет обработано в следующей функции salary и запись в record_s
            bot.register_next_step_handler(msg, record_s)

            bot.register_next_step_handler(msg, prepay)

        else:
            # если будет отправлено что-то иное - возврат в предыдущее меню
            monthes(message)
            return


# запись ответа (оклад)

def record_s(message):
    global salary_u
    salary_u = int(message.text)
    return salary_u


 # Количество рабочих, праздничных дней в месяце
 # расчет количества рабочих дней в первой и второй половине месяца

def day():
     global holidays
     global businessdays
     global firsthalf
     global secondhalf

     now = datetime.datetime.now()
     year = now.year

     # Количество праздничных дней


     if month == 1:
         holidays = [datetime.date(year, month, 1),  # год, месяц, праздничное число
                     datetime.date(year, month, 2),
                     datetime.date(year, month, 3),
                     datetime.date(year, month, 4),
                     datetime.date(year, month, 5),
                     datetime.date(year, month, 6),
                     datetime.date(year, month, 7),
                     datetime.date(year, month, 8),
                     datetime.date(year, month, 9)
                     ]
     elif month == 2:
         holidays = [datetime.date(year, month, 23)]
     elif month == 3:
         holidays = [datetime.date(year, month, 7),
                     datetime.date(year, month, 7)
                     ]
     elif month == 4:
         holidays = [0]
     elif month == 5:
         holidays = [datetime.date(year, month, 2),
                     datetime.date(year, month, 3),
                     datetime.date(year, month, 9),
                     datetime.date(year, month, 10)
                     ]
     elif month == 6:
         holidays = [datetime.date(year, month, 13)]
     elif month == 7:
         holidays = [0]
     elif month == 8:
         holidays = [0]
     elif month == 9:
         holidays = [0]
     elif month == 10:
         holidays = [0]
     elif month == 11:
         holidays = [datetime.date(year, month, 4)]
     elif month == 12:
         holidays = [datetime.date(year, month, 31)]


     # Количество рабочих дней

     businessdays = 0
     for i in range(1, 32):
         try:
             thisdate = datetime.date(year, month, i)
         except(ValueError):
             break
         if thisdate.weekday() < 5 and thisdate not in holidays:  # Monday == 0, Sunday == 6; thisdate.weekday() - показывет порядковый номер дня недели для числа i
             businessdays += 1

     # Количество рабочих дней до 15 числа

     firsthalf = 0
     for a in range(1, 16):
         try:
             thisdate = datetime.date(year, month, a)
         except(ValueError):
             break
         if thisdate.weekday() < 5 and thisdate not in holidays:
             firsthalf += 1

     # Количество рабочих дней после 15 числа

     secondhalf = 0
     for a in range(16, 32):
         try:
             thisdate = datetime.date(year, month, a)
         except(ValueError):
             break
         if thisdate.weekday() < 5 and thisdate not in holidays:
             secondhalf += 1

     return holidays, businessdays, firsthalf, secondhalf
     # return businessdays
     # return firsthalf
     # return secondhalf


# Расчет

def prep():
     global oklad
     global avans
     global zp
     # кнопки
     cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
     cancel.row('В начало')

     # расчет и вывод оклада с НДС
     oklad = round((salary_u - ((salary_u * 13) / 100)), 2)
     # print('Оклад с НДС:', oklad)

     day()

     # расчет и вывод аванса с НДС
     avans = round(((oklad / businessdays) * firsthalf), 2)
     zp = round(((oklad / businessdays) * secondhalf), 2)
     # print('Аванс: ', avans)

     return avans, zp


# Расчет аванса
@bot.message_handler(content_type=['text'])
def prepay(message):
    # кнопки
    cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cancel.row('В начало')

    if message.text.isdigit():
        prep()

        msg = bot.send_message(message.from_user.id, avans)
        msg = bot.send_message(message.from_user.id, zp)

        msg = bot.send_message(message.from_user.id, 'Для повторного расчета нажми "/start"', reply_markup=cancel)

        bot.register_next_step_handler(msg, start)


def start(message):
    if message.text == '/start' or message.text == 'В начало':
        send_welcome(message)


#проверка на новые сообщения
bot.polling(none_stop=True, interval=0)

