# filter().py

def func(a):
    if a <100:
        return True
    else:
        return False

print(list(filter(func,[10,56,101,500])))
# 返回True所对应的值


def f(x):
    x = 100
    print(x)

a = 1
f(a)
print(a)
