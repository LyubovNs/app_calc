import datetime

now = datetime.datetime.now()
holidays = {datetime.date(now.year, 8, 14)} # you can add more here
businessdays = 0
for i in range(1, 32):
    try:
        thisdate = datetime.date(now.year, now.month, i)
    except(ValueError):
        break
    if thisdate.weekday() < 5 and thisdate not in holidays: # Monday == 0, Sunday == 6
        businessdays += 1

print (businessdays)


#
# import calendar
#
# weekday_count = 0
# cal = calendar.Calendar()
#
# for week in cal.monthdayscalendar(2013, 8):
#     for i, day in enumerate(week):
#         # not this month day or a weekend
#         if day == 0 or i >= 5:
#             continue
#         # or some other control if desired...
#         weekday_count += 1
#
# print weekday_count