'''
#自定义函数模板
def functionname( 参数、自变量 ): --冒号表示函数起始 / def --函数头关键字
   "函数_文档字符串" --存放函数说明
   function_suite
   return [expression] --结束函数并返回值，不带表达式则返回none
'''
'''
def printme( str ):
   "打印传入的字符串到标准显示设备上"
   print(str)
   return #返回值为none
'''

# Function definition is here
def printme( str ):
   "打印任何传入的字符串"
   print(str)
   return
 
# Now you can call printme function
printme("我要调用用户自定义函数!")
printme("再次调用同一函数")
printme("这就是自定义函数条用命令")
