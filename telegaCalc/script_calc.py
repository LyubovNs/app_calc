# import calendar
import datetime
# import weekday
import telebot
from telebot import types

# определение текущего времени и года
from telegram import message

now = datetime.datetime.now()
year = now.year

# узнать количество дней в месяце
# y = int(input('Введите год: '))
# m = int(input('Введите месяц: '))
# print(calendar.monthrange(y, m)[1])
# количество дней в месяце
# days = int((calendar.monthrange(year, month)[1]))


# Расчет аванса и зарплаты
# ввод суммы аклада и расчетного месяца

print('Расчет аванса и зарплаты')

# ввод суммы аклада
while True:
    try:
        oklad = int(input('Введите оклад за месяц с НДС: '))
        if oklad > 0:
            break
        else:
            print('Введенное число меньше нуля')
    except ValueError:
        print("Вы ввели не число. Попробуйте снова: ")


# расчет оклада без НДС
# oklad = oklad - (oklad/100)*13

# ввод расчетного месяца
def month():
    if message.text == 'Январь':
        month = 1
    elif message.text  == 'Февраль':
        month = 2
    elif message.text  == 'Март':
        month = 3
    elif message.text  == 'Апрель':
        month = 4
    elif message.text  == 'Май':
        month = 5
    elif message.text  == 'Июнь':
        month = 6
    elif message.text  == 'Июль':
        month = 7
    elif message.text  == 'Август':
        month = 8
    elif message.text  == 'Сентябрь':
        month = 9
    elif message.text  == 'Октябрь':
        month = 10
    elif message.text  == 'Ноябрь':
        month = 11
    elif message.text  == 'Декабрь':
        month = 12



# Количество праздничных дней в месяце

# [datetime.datetime(2022, 1, 3), datetime.datetime(2022, 3, 3), datetime.datetime(2022, 4, 22), datetime.datetime(2022, 4, 25)]

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


# Расчет оклада и аванса

# вывод оклада без НДС
print('Оклад без НДС:', oklad)

# расчет и вывод оклада с НДС
oklad = round((oklad - ((oklad * 13) / 100)), 2)
print('Оклад с НДС:', oklad)

# расчет и вывод аванса с НДС
avans = round(((oklad / businessdays) * firsthalf), 2)
print('Аванс: ', avans)


# Расчет оклада и зарплаты

# вывод оклада без НДС

print('Оклад без НДС:', oklad)

# расчет и вывод оклада с НДС
oklad = round((oklad - ((oklad * 13) / 100)), 2)
print('Оклад с НДС:', oklad)

# расчет и вывод зарплаты с НДС
zp = round(((oklad / businessdays) * secondhalf), 2)
print('Зарплата: ', zp)