#输出日历
import calendar

cal = calendar.month(2008, 6)
print("Here is the calendar:")
print(cal)

#输出格式化时间
import time

localtime = time.asctime( time.localtime(time.time()) )
print("Local current time :", localtime)
