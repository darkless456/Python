# 调用printme()函数，你必须传入一个参数，不然会出现语法错误

#可写函数说明
def printme( str ):
   "打印任何传入的字符串"
   print(str)
   return
 
#调用printme函数
printme( ) # 错误写法，必备参数str没有传入。
