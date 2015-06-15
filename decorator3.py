# decorator.py

import time

def foo():
    print('in foo()')
    return

def timeIt(func):
    def wrapper():
        start = time.clock()
        func()
        end = time.clock()
        print('used:', end - start)
        return
    return wrapper

# 装饰器实质
'''
@timeIt
def foo():
    print('in foo()')
    return
'''
foo = timeIt(foo)
foo()
