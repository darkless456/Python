# time.py

class Time(object):
    def __str__(self):
        return '%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)

time = Time (9,45)
print(time)

# 有错误
