# coding:utf8
# def_function.py

def print_two (*args): # 参数个数不确定
    arg1, arg2 = args  # 参数解包
    print ("arg1: %r, arg2: %r"% (arg1, arg2)) # 传递参数
    return

def print_two_again (arg1, arg2):
    print ("arg1: %r, arg2: %r"% (arg1, arg2))
    return

def print_one (arg1):
    print ("arg1: %r"% arg1)
    return

def print_none():
    print ("I go nothing.")
    return

print_two ("kevin", "bob")
print_two ('kevin', 'bob')
print_one ("hello")
print_none()
