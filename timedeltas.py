from datetime import date, time, datetime
from datetime import timedelta

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
print('Today is: ' + str(now))

print('One year from now it will be: ' + str(now + timedelta(days=365)))
