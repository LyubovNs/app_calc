import datetime

now = datetime.datetime.now()
year = now.year
# узнать количество дней в месяце
# y = int(input('Введите год: '))
# m = int(input('Введите месяц: '))
# print(calendar.monthrange(y, m)[1])
# количество дней в месяце
# days = int((calendar.monthrange(year, month)[1]))

# print('Расчет аванса')
# oklad = int(input('Введите оклад за месяц: '))
month = 5

# вывести календарь месяца
# print ('Календарь для', month, year, 'is: ')
# print (calendar.month(month, 3, 2, 1))
i=5
thisdate = datetime.date(year, month, i)

holidays = {datetime.date(year, month, 1)}
print(holidays)

print(thisdate.weekday())

# < 5 and thisdate not in holidays:  # Monday == 0, Sunday == 6

holidays = [{datetime.date(year, month, 1)},  # год, месяц, праздничное число
            {datetime.date(year, month, 2)},
            {datetime.date(year, month, 3)},
            {datetime.date(year, month, 4)},
            {datetime.date(year, month, 5)},
            {datetime.date(year, month, 6)},
            {datetime.date(year, month, 7)},
            {datetime.date(year, month, 8)},
            {datetime.date(year, month, 9)}
            ]

print(holidays)