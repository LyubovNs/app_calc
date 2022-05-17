import calendar
import datetime
import weekday

now = datetime.datetime.now()
year = now.year
# month = 3
holidays = {datetime.date(year, month, 7)}


businessdays = 0
for i in range(1, 31):
    try:
        thisdate = datetime.date(year, month, i)
    except(ValueError):
        break
    if thisdate.weekday() < 5 and thisdate not in holidays: # Monday == 0, Sunday == 6
        businessdays += 1
print ('Количество рабочих дней: ', businessdays)

firsthalf = 0
for a in range (1,15):
    try:
        thisdate = datetime.date(year, month, a)
    except(ValueError):
         break
    if thisdate.weekday() < 5 and thisdate not in holidays:
        firsthalf += 1
print('Количество рабочих дней до 15 числа: ', firsthalf)

secondhalf = 0
for a in range (15,31):
    try:
        thisdate = datetime.date(year, month, a)
    except(ValueError):
         break
    if thisdate.weekday() < 5 and thisdate not in holidays:
        secondhalf += 1
print('Количество рабочих дней после 15 числа: ', secondhalf)


holidays = {datetime.date(year, month, 2)}
print(holidays)