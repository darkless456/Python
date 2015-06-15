'''
def square_sum(a,b):
    print("input: ", a, b)
    return a**2 + b**2

def square_diff(a,b):
    print("input: ", a, b)
    return a**2 - b**2

print(square_sum(5,6))
print(square_diff(5,4))
'''

def decorator(G): # 定义一个装饰函数，通用的
    def G2(a,b):
        print("input:", a,b)
        return G(a,b)
    return G2

@decorator # 调用装饰函数
def square_sum(a, b):
    return a**2 + b**2
'''
square_sum = decorator(square_sum)
square_sum(3, 4)
'''

@decorator
def square_diff(a, b):
    return a**2 - b**2

print(square_sum(5,6))
print(square_diff(5,4))
