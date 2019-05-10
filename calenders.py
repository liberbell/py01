import calendar

c = calendar.TextCalendar(calendar.MONDAY)
# st = c.formatmonth(2019, 5, 0, 0)
# print(st)

# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2019, 5)
# print(st)

# for i in c.itermonthdays(2019, 5):
#     print(i)

# for name in calendar.month_name:
#     print(name)
#
# for day in calendar.day_name:

print('Team meeting will be on: ')
for m in ragen(1, 13):
    cal = calendar.monthcalendar(2019, m)
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        meetday = weektwo[calendar.FRIDAY]
