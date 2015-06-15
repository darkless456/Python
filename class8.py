# class.py

class GrandPa(object):
    def __init(self):
        print('I\'m GrandPa.')

class Father(GrandPa):
    def __init__(self):
        print('I\'m Father.')
    def print_fun(self):
        print('I\'m father_class.')

class Son(Father):
    def __init__(self):
        print('I\'m 构造函数，son.')
    def sayHello(self):
        return 'hello world'

if __name__ == '__main__':
    son = Son() # 实例化
    print(Son.__name__)
    son.print_fun() # 引用父类的方法
