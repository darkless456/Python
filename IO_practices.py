# coding:utf8
# fileName:IO_practices.py

from sys import argv

script, fileName = argv # 前3行语句用来获取filename

prompt = ">> " # 定义输出时符号

txt = open (fileName) # open命令接受了参数fileName并把它赋值给txt变量

print ("Here's your file %r:"% fileName)
print (txt.read()) # read()读取txt变量的内容并打印


print ("Type the filename again:")
file_again = input (prompt)

txt_again = open (file_again)

print (txt_again.read())
txt_again.close() # 关闭文件
