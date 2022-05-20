# import calendar
import datetime
# import weekday

# определение текущего времени и года

now = datetime.datetime.now()
year = now.year

# Количество праздничных дней в месяце

# [datetime.datetime(2022, 1, 3), datetime.datetime(2022, 3, 3), datetime.datetime(2022, 4, 22), datetime.datetime(2022, 4, 25)]
def holi(month):
    global holidays
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

    print(holidays)


holi()