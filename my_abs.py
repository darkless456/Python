# my_abs.py

#coding:utf-8

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad type')
    if x >= 0:
        return x
    else:
        return -x
    
a = input('the input num: ') # 默认输入为string
my_abs(a)
 
