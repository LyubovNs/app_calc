# import calendar
import datetime
# import weekday

# определение текущего времени и года

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
while True:
    try:
        month = int(input('Введите цифру месяца: '))
        if month == 1:
            print('Январь')
            break
        elif month == 2:
            print('Февраль')
            break
        elif month == 3:
            print('Март')
            break
        elif month == 4:
            print('Апрель')
            break
        elif month == 5:
            print('Май')
            break
        elif month == 6:
            print('Июнь')
            break
        elif month == 7:
            print('Июль')
            break
        elif month == 8:
            print('Август')
            break
        elif month == 9:
            print('Сентябрь')
            break
        elif month == 10:
            print('Октябрь')
            break
        elif month == 11:
            print('Ноябрь')
            break
        elif month == 12:
            print('Декабрь')
            break
        else:
            print('Введенное число вне диапазона от 1 до 12')
    except ValueError:
        print("Вы ввели не число. Попробуйте снова: ")



# Количество праздничных дней в месяце

# [datetime.datetime(2022, 1, 3), datetime.datetime(2022, 3, 3), datetime.datetime(2022, 4, 22), datetime.datetime(2022, 4, 25)]
def holiday ():
    if month == 'Январь':
        global holidays
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

    elif month == 'Февраль':
        holidays = [datetime.date(year, month, 23)]
    elif month == 'Март':
        holidays = [datetime.date(year, month, 7),
                    datetime.date(year, month, 7)
                   ]
    elif month == 'Апрель':
        holidays = [0]
    elif month == 'Май':
        holidays = [datetime.date(year, month, 2),
                    datetime.date(year, month, 3),
                    datetime.date(year, month, 9),
                    datetime.date(year, month, 10)
                    ]
    elif month == 'Июнь':
        holidays = [datetime.date(year, month, 13)]
    elif month == 'Июль':
        holidays = [0]
    elif month == 'Август':
        holidays = [0]
    elif month == 'Сентябрь':
        holidays = [0]
    elif month == 'Октябрь':
        holidays = [0]
    elif month == 'Ноябрь':
        holidays = [datetime.date(year, month, 4)]
    elif month == 'Декабрь':
        holidays = [datetime.date(year, month, 31)]

    return holidays

# вывести календарь месяца
# print ('Календарь для', month, year, 'is: ')
# print (calendar.month(month, 3, 2, 1))

# Количество рабочих дней в месяце

def businessdays():
    global businessdays
    businessdays = 0
    for i in range(1, 32):
        try:
            thisdate = datetime.date(year, month, i)
        except(ValueError):
            break
        if thisdate.weekday() < 5 and thisdate not in holidays(): # Monday == 0, Sunday == 6; thisdate.weekday() - показывет порядковый номер дня недели для числа i
            businessdays += 1
# print ('Количество рабочих дней: ', businessdays)
    return businessdays

# Количество рабочих дней до 15 числа

def first():
    global firsthalf
    firsthalf = 0
    for a in range (1,16):
        try:
            thisdate = datetime.date(year, month, a)
        except(ValueError):
            break
        if thisdate.weekday() < 5 and thisdate not in holidays():
            firsthalf += 1
# print('Количество рабочих дней до 15 числа: ', firsthalf)
    return firsthalf


# Количество рабочих дней после 15 числа

def secondhalf():
    global secondhalf
    secondhalf = 0
    for a in range (16,32):
        try:
            thisdate = datetime.date(year, month, a)
        except(ValueError):
         break
        if thisdate.weekday() < 5 and thisdate not in holidays():
            secondhalf += 1
# print('Количество рабочих дней после 15 числа: ', secondhalf)
    return secondhalf

# Расчет оклада, аванса и зарплаты, вывод

# вывод оклада без НДС
print('Оклад без НДС:', oklad)

# расчет и вывод оклада с НДС
oklad = round((oklad - ((oklad * 13) / 100)), 2)
print('Оклад с НДС:', oklad)

# расчет и вывод аванса с НДС
avans = round(((oklad / businessdays()) * firsthalf()), 2)
print('Аванс: ', avans)

# расчет и вывод зарплаты с НДС
zp = round(((oklad / businessdays()) * secondhalf()), 2)
print('Зарплата: ', zp)
