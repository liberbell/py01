import calendar

c = calendar.TextCalendar(calendar.MONDAY)
# st = c.formatmonth(2019, 5, 0, 0)
# print(st)

# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# st = hc.formatmonth(2019, 5)
# print(st)

for i in c.itermonthdays(2019, 5):
    print(i)
