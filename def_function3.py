# coding:utf-8
# def_function3.py
# 标明序号

from sys import argv

script, input_file = argv

def print_all (f):
    print (f.read()) # 输出文件f的内容

def rewind (f):
    f.seek (0) # 重新定位在文件f的第0位/起始位置

def print_a_line (line_count, f):
    print (line_count, f.readline()) # readline读取文件一行

current_file = open (input_file, 'r+') # 传递文件属性、内容

print ("First let's print the whole file:\n")
print_all (current_file) # 打印初始文件

print ("Now let's rewind, kind of like a tape.")
rewind (current_file) # 回到文件起始位置

print ("Let's print three lines: ")

current_line = 1 # 赋值
print_a_line (current_line, current_file) # 打印1 和 初始文件第1行

current_line = current_line + 1 # 2
print_a_line (current_line, current_file) # 打印2 和 初始文件第2行

current_line = current_line + 1 # 3
print_a_line (current_line, current_file)
