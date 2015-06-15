# time.py

import time as time1

print(time1.time())
print("\v")
print(time1.localtime(time1.time()))
print("\v")
print(time1.strftime('%Y-%m-%d', time1.localtime(time1.time())))
print(time1.strftime('%y/%m/%d  %I:%M:%S %p 今年第%j天,第%U周 星期%w 名称:%A, 月份:%B', \
                     time1.localtime(time1.time())))
print('\v')
print(time1.strftime('本地时间：%X 时区：%Z', time1.localtime(time1.time())))
