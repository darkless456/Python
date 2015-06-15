# fileName: Fibonacci numbers module

def fib (n):
    "求Fibonacci数列"
    a , b = 0 ,1
    while b < n :
        print (b , end=' ,') #end=' ,' 输出的分隔符
        a , b = b , a+b
    print ()


def fib2 (n):
    "用list求Fibonacci数列"
    result = [] # 创建空list
    a , b = 0 , 1
    while b < n:
        result[len(result):] = [b] # result.append (b) 在list尾添加元素
        a ,b = b , a+b
    return result
