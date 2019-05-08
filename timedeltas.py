from datetime import date, time, datetime
from datetime import timedelta

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
print('Today is: ' + str(now))

print('One year from now it will be: ' + str(now + timedelta(days=365)))

print('In 2 days and 3 weeks, It will be: ' + str(now + timedelta(days=2, weeks=3)))
t = datetime.now() - timedelta(weeks=1)
s = t.strftime('%A %B %d, %Y')
print('One week ago it was: ' + s)

today = date.today()
afd = date(today.year, 4, 1)
print('This year april fool`s date: ' + str(afd))

if afd < today:
    print('April Fool`s day already went by %d days ago' % (today - afd).days)
    afd = afd.replace(year = today.year+1)

time_to_afd = afd - today
print('It`s just ', time_to_afd.days, 'days until April Fool`s day')
