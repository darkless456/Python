#class.py

class bird(object):
    feather = True

class chicken(bird):
    fly = False
    def __init__(self,age):
        self.age = age
    def getAdult(self):
        if self.age > 1:
            return True
        else:
            return False
    adult = property(getAdult)
    '''特性使用内置函数property()来创建。
property()最多可以加载四个参数。前三个参数为函数，分别用于
处理查询特性、修改特性、删除特性。最后一个参数为特性的文档，
可以为一个字符串，起说明作用。'''

summer = chicken(0.9)

print(summer.adult)
summer.age = 1.5
print(summer.adult)
