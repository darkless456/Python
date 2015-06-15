# timing.py

import datetime, calendar

today = datetime.date.today()

yesterday = today - datetime.timedelta(days = 1)

tomorrow = today + datetime.timedelta(days = 1)

print(yesterday, today, tomorrow)

# -------------------------
'''
last_friday = datetime.date.today()
oneday = datetime.timedelta(days = 1)

while last_friday.weekday() != calendar.FRIDAY :
    last_friday = oneday

print(last_friday.strftime('%A, %d-%b-%Y'))
'''
t = datetime.datetime(2012,9,3,21,30)
k = datetime.date.today()
print(t, '\n', k)
