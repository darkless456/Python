def return_Sum (x,y) :
    c = x + y
    return c     # 函数的返回值，可理解为函数自运行完成后的结果

res = return_Sum (4,5)
print (res)

print ("*"*50)
print ()


print ("以下是可变参数函数")
print ()

def func2 (*args) :
    sum = 0
    for x in args :
        sum += x
    return sum

print (func2 (45,32,44))
print ("*"*50)
print (func2 (1,1,1))
print ("*"*50)
print (func2 ())
