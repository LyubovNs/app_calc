import telebot
import datetime
from functools import wraps
from kod_v2 import month

now = datetime.datetime.now()
year = now.year

#указание токена бота
from telegram import message

token = '5352935775:AAENA4YzYLSlHp6jqdfI3mR9wOK89o7aGaw'

# запрет на отправку собщений всем, крме админа

LIST_OF_ADMINS = [378989143]

def restricted(func):
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in LIST_OF_ADMINS:
            print("Unauthorized access denied for {}.".format(user_id))
            return
        return func(update, context, *args, **kwargs)
    return wrapped


# получение расчетного месяца
def month_check():
    month =
    if month == 'Январь':
        month_n = 1
    elif month  == 'Февраль':
        month_n = 2
    elif month  == 'Март':
        month_n = 3
    elif month  == 'Апрель':
        month_n = 4
    elif month  == 'Май':
        month_n = 5
    elif month  == 'Июнь':
        month_n = 6
    elif month  == 'Июль':
        month_n = 7
    elif month  == 'Август':
        month_n = 8
    elif month  == 'Сентябрь':
        month_n = 9
    elif month  == 'Октябрь':
        month_n = 10
    elif month  == 'Ноябрь':
        month_n = 11
    elif month  == 'Декабрь':
        month_n = 12


# Количество праздничных дней в месяце

def holiday():
    if month == 1:
        holidays = [datetime.date(year, month, 1),   #год, месяц, праздничное число
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



# вывести календарь месяца
# print ('Календарь для', month, year, 'is: ')
# print (calendar.month(month, 3, 2, 1))

# Количество рабочих дней в месяце

businessdays = 0
for i in range(1, 32):
    try:
        thisdate = datetime.date(year, month, i)
    except(ValueError):
        break
    if thisdate.weekday() < 5 and thisdate not in holidays: # Monday == 0, Sunday == 6; thisdate.weekday() - показывет порядковый номер дня недели для числа i
        businessdays += 1
print ('Количество рабочих дней: ', businessdays)


# Количество рабочих дней до 15 числа

firsthalf = 0
for a in range (1,16):
    try:
        thisdate = datetime.date(year, month, a)
    except(ValueError):
        break
    if thisdate.weekday() < 5 and thisdate not in holidays:
        firsthalf += 1

print('Количество рабочих дней до 15 числа: ', firsthalf)


# Количество рабочих дней после 15 числа

secondhalf = 0
for a in range (16,32):
    try:
        thisdate = datetime.date(year, month, a)
    except(ValueError):
     break
    if thisdate.weekday() < 5 and thisdate not in holidays:
        secondhalf += 1

print('Количество рабочих дней после 15 числа: ', secondhalf)
