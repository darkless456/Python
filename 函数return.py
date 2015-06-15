# 可写函数说明
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print("Inside the function : ", total)   # 内取值
   return total
 
# 调用sum函数
total = sum( 10, 20 );
# print("Outside the function : ", total)  # 外取值
