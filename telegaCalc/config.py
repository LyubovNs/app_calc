import telebot
import datetime
from telegram import message

# import kod_v2
# from kod_v2 import record_m, record_s
# from functools import wraps     запрет на отправку собщений всеми, крме админа


#указание токена бота
token = '5352935775:AAENA4YzYLSlHp6jqdfI3mR9wOK89o7aGaw'


# запрет на отправку собщений всеми, крме админа
# LIST_OF_ADMINS = [378989143]
#
# def restricted(func):
#     @wraps(func)
#     def wrapped(update, context, *args, **kwargs):
#         user_id = update.effective_user.id
#         if user_id not in LIST_OF_ADMINS:
#             print("Unauthorized access denied for {}.".format(user_id))
#             return
#         return func(update, context, *args, **kwargs)
#     return wrapped


# ПЕРЕНЕСЕНО В KOD_V3!!!!
#
# # получение расчетного месяца
# # изъятие сообщения пользователя
# def get_m():
#     global month_u
#     month_u = kod_v2.record_m()
#
#
# # нумерация месяцов
# def month_check():
#     global month
#     if month_u == 'Январь':
#         month = 1
#     elif month_u  == 'Февраль':
#         month = 2
#     elif month_u  == 'Март':
#         month = 3
#     elif month_u  == 'Апрель':
#         month = 4
#     elif month_u  == 'Май':
#         month = 5
#     elif month_u  == 'Июнь':
#         month = 6
#     elif month_u  == 'Июль':
#         month = 7
#     elif month_u  == 'Август':
#         month = 8
#     elif month_u  == 'Сентябрь':
#         month = 9
#     elif month_u  == 'Октябрь':
#         month = 10
#     elif month_u  == 'Ноябрь':
#         month = 11
#     elif month_u  == 'Декабрь':
#         month = 12
#
#
# # Количество рабочих, праздничных дней в месяце
# # расчет количества рабочих дней в первой и второй половине месяца
#
# def day():
#     global holidays
#     global businessdays
#     global firsthalf
#     global secondhalf
#
#     now = datetime.datetime.now()
#     year = now.year
#
#
# # Количество праздничных дней
#
#     if month == 1:
#         holidays = [datetime.date(year, month, 1),   #год, месяц, праздничное число
#                     datetime.date(year, month, 2),
#                     datetime.date(year, month, 3),
#                     datetime.date(year, month, 4),
#                     datetime.date(year, month, 5),
#                     datetime.date(year, month, 6),
#                     datetime.date(year, month, 7),
#                     datetime.date(year, month, 8),
#                     datetime.date(year, month, 9)
#                     ]
#     elif month == 2:
#          holidays = [datetime.date(year, month, 23)]
#     elif month == 3:
#          holidays = [datetime.date(year, month, 7),
#                      datetime.date(year, month, 7)
#                     ]
#     elif month == 4:
#         holidays = [0]
#     elif month == 5:
#         holidays = [datetime.date(year, month, 2),
#                     datetime.date(year, month, 3),
#                     datetime.date(year, month, 9),
#                     datetime.date(year, month, 10)
#                     ]
#     elif month == 6:
#         holidays = [datetime.date(year, month, 13)]
#     elif month == 7:
#          holidays = [0]
#     elif month == 8:
#         holidays = [0]
#     elif month == 9:
#         holidays = [0]
#     elif month == 10:
#         holidays = [0]
#     elif month == 11:
#         holidays = [datetime.date(year, month, 4)]
#     elif month == 12:
#          holidays = [datetime.date(year, month, 31)]
#
#     return holidays
#
# # Количество рабочих дней
#
#     businessdays = 0
#     for i in range(1, 32):
#             try:
#                 thisdate = datetime.date(year, month, i)
#             except(ValueError):
#                         break
#             if thisdate.weekday() < 5 and thisdate not in holidays: # Monday == 0, Sunday == 6; thisdate.weekday() - показывет порядковый номер дня недели для числа i
#                 businessdays += 1
#
#     return businessdays
#
#     # print ('Количество рабочих дней: ', businessdays)
#
# # Количество рабочих дней до 15 числа
#
#     firsthalf = 0
#     for a in range (1,16):
#         try:
#             thisdate = datetime.date(year, month, a)
#         except(ValueError):
#             break
#         if thisdate.weekday() < 5 and thisdate not in holidays:
#             firsthalf += 1
#
#     return firsthalf
#
#     # print('Количество рабочих дней до 15 числа: ', firsthalf)
#
# # Количество рабочих дней после 15 числа
#
#     secondhalf = 0
#     for a in range (16,32):
#         try:
#             thisdate = datetime.date(year, month, a)
#         except(ValueError):
#             break
#         if thisdate.weekday() < 5 and thisdate not in holidays:
#             secondhalf += 1
#
#     return secondhalf
#
#     # print('Количество рабочих дней после 15 числа: ', secondhalf)
#
#
# # расчет аванса
# # вывод оклада без НДС
#
# # получение оклада из сообщения пользователя
#
# def get_s():
#     global salary_u
#     salary_u = kod_v2.record_s()
# # print('Оклад без НДС:', salary_u)
#
#
# def prep():
#     global oklad
#     global avans
#
#     # расчет и вывод оклада с НДС
#     oklad = round((salary_u - ((salary_u * 13) / 100)), 2)
#     # print('Оклад с НДС:', oklad)
#
#     # расчет и вывод аванса с НДС
#     avans = round(((oklad / businessdays) * firsthalf), 2)
#     # print('Аванс: ', avans)
#
#     return avans