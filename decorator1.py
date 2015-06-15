# decorator.py

def deco(func):
    print('ok')
    return func

@deco
def foo():
    print('foo')
foo()

# ---------等价于-----------
print("-"*10 ,  '等价于', '-'*10)

def deco1(func):
    print('ok')
    return func
def foo():
    print('foo')
deco1(foo)
foo()
