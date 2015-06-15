# 变量的作用域

total = 0 # total在这里是全局变量 
# 可写函数说明
def sum( arg1, arg2 ):
   #返回2个参数的和."
   total = arg1 + arg2; # total在这里是局部变量.
   print("Inside the function local total : ", total)
   return total
 
#调用sum函数
sum( 10, 20 ) # 输出局部变量total
print("Outside the function global total : ", total) # 输出全局变量total 
