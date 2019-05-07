from datetime import date, time, datetime
from datetime import timedelta

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
print('Today is: ' + str(now))

print('One year from now it will be: ' + str(now + timedelta(days=365)))

print('In 2 days and 3 weeks, It will be: ' + str(now + timedelta(days=2, weeks=3)))
t = datetime.now() - timedelta(weeks=1)
s = t.strftime('%A %B %d, %Y')
print(s)
