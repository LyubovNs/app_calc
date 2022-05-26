# рабочий код на одну кнопку
# сделан вывод сумм в одном сообщении
# настроены кнопки назад из каждого подменю
# сделана проверка на ввод оклада

import telebot
from telebot import types
import logging
import datetime

from telegram import message

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
        u'Здравствуй, {name}\n'
        u'Я умею рассчитывать аванс и зарплату, но пока не умею считать отпускные.\n\n'
        u'Нажимай: "Хочу зарплату и аванс"',

    'help':
        u'Нажимай: "Хочу зарплату и аванс"',

    'Назад':
        u'Назад'
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
    markup.row('Хочу зарплату и аванс')

    # сообщение пользователю - приветствие
    msg = bot.send_message(message.from_user.id, welcome_message['start'].format(name=message.from_user.first_name), reply_markup=markup)

    # для связи функци - принимает в себя сообщение из текущей и говорит о том, что оно будет обработано в следующей функции monthes
    bot.register_next_step_handler(msg, monthes)


# функция выбора месяца

@bot.message_handler(content_type=['text'])
def monthes(message):
    # кнопки
    m = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # проверка работы предыдущей функции
    if message.text == 'Хочу зарплату и аванс' or message.text == '/start' or message.text == 'Назад':
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


# запись ответа (месяц)

def record_m(message):
    global month_u
    # для возврата в предыдущее меню send_welcome
    if message.text == 'Назад':
       send_welcome(message)
       return
    # переход в функцию нумерации месяцев
    else:
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
    mon_r = types.ReplyKeyboardMarkup(resize_keyboard=True)
    mon_r.row('Назад')

    # проверка работы предыдущей функции monthes - на верный ввод месяца
    if message.text == 'Январь' or message.text == 'Февраль' \
            or message.text == 'Март' or message.text == 'Апрель' \
            or message.text == 'Май' or message.text == 'Июнь' or message.text == 'Июль' \
            or message.text == 'Август' \
            or message.text == 'Сентябрь' or message.text == 'Октябрь' \
            or message.text == 'Ноябрь' \
            or message.text == 'Декабрь':\
            # сообщение пользователю ввести оклад
            msg = bot.send_message(message.from_user.id, 'Введите оклад за месяц с НДС', reply_markup=mon_r)
            # для связи функци - принимает в себя сообщение из текущей и говорит о том, что оно будет обработано в следующей функции salary и запись в record_s
            bot.register_next_step_handler(msg, record_s)
            # bot.register_next_step_handler(msg, prepay)


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


# запись ответа (оклад) и проверка введенного в salary(message)

# def record_s(message):
#     global salary_u
#
#     if message.text == 'Назад':
#         monthes(message)
#     else:
#         salary_u = message.text
#         try:
#             if salary_u.isdigit():
#                 salary_u = int(message.text)
#                 return salary_u
#                 prep()
#         except ValueError:
#             bot.send_message(message.from_user.id, 'Не понимаю, начни заново - /start')


def record_s(message):
    global salary_u
     # возврат в предыдущее меню для выбора месяца - monthes
    if message.text == 'Назад':
        monthes(message)
    # проверка, что введенный оклад - число и переход к функции вычисления prep
    elif message.text.isdigit():
        salary_u = message.text
        prepay(message)

        # return salary_u
        # bot.register_next_step_handler(msg, prep)
    else:
    # обработка ввода текстовых символов - запись в верного значения в record_s и в prepay
        try:
            msg = bot.send_message(message.from_user.id, 'Не понимаю, введи число или нажми "Назад"')
            bot.register_next_step_handler(msg, record_s)   #за счет записи в саму себя будет работать до тех пора, пока не будет введено число
            # bot.register_next_step_handler(msg, prepay)
        except ValueError:
            msg = bot.send_message(message.from_user.id, 'Не понимаю, введи число или начни заново /start')


# Расчет аванса и зарплаты

def prep():
     global oklad
     global avans
     global zp

     num = int(salary_u)

     # расчет и вывод оклада с НДС
     oklad = round((num - ((num * 13) / 100)), 2)
     # print('Оклад с НДС:', oklad)

     # вызов функции для расчета рабочих, праздничны дней
     day()

     # расчет и вывод аванса с НДС
     avans = round(((oklad / businessdays) * firsthalf), 2)
     zp = round(((oklad / businessdays) * secondhalf), 2)
     # print('Аванс: ', avans)

     return avans, zp


# Вывод аванса и зарплаты
@bot.message_handler(content_type=['text'])
def prepay(message):
    # кнопки
    cancel = types.ReplyKeyboardMarkup(resize_keyboard=True)
    cancel.row('В начало')

    # if message.text == 'Назад':   #закомментировано, так как проверка предыдущей функции def salary(message) выполняется в record_s
    #     monthes(message)
    # if message.text.isdigit():
    prep()
    msg = bot.send_message(message.from_user.id, (f'Аванс: {avans}\n' 
                                                  f'Зарплата: {zp}'))
    # для связи функци - принимает в себя сообщение из текущей и говорит о том, что оно будет обработано в следующей функции start для возврата в главное меню
    msg = bot.send_message(message.from_user.id, 'Для повторного расчета нажми "/start"', reply_markup=cancel)
    bot.register_next_step_handler(msg, start)
    # else:
    salary(message)


# Переход к началу
def start(message):
    if message.text == '/start' or message.text == 'В начало':
        send_welcome(message)


# проверка на новые сообщения
bot.polling(none_stop=True, interval=0)

