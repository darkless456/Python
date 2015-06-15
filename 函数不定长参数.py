# 可写函数说明
def printinfo( arg1, *vartuple ): # 加了星号（*）的变量名会存放所有未命名的变量参数
   "打印任何传入的参数"
   print("输出: ")
   print(arg1)
   for var in vartuple:
      print(var)
   return
 
# 调用printinfo 函数
printinfo( 10 )
printinfo( 70, 60, 50 )
