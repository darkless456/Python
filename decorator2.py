# decorator.py

from time import ctime
from time import sleep

def deco(func):
    def decoIn():
        print('[%s]:%s called' %(ctime(), func.__name__))
        return func
    return decoIn
'''
装饰函数的参数是被装饰的函数对象，返回原函数对象
装饰的实质语句: foo = deco(foo)
'''
@deco
def foo():
    pass
foo()
sleep(1)

for i in range(4):
    sleep(1)
    foo()
    
