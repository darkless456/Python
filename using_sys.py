# fileName: using_sys.py

import sys # 引入标准库中sys.py模块
# from sys import *  错误语句

print ("命令行参数如下：")
for i in sys.argv: # sys.argv是一个包含命令行参数的list
    print (i)

print ('***The PYTHONPATH is', sys.path, '***') # sys.path包含所需模块的路径的列表。 
