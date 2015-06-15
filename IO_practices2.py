# coding:utf8
# IO_practices2.py

from sys import argv

script, fileName = argv
prompt = ">>"

print ("We're going to erase %r."% fileName)
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit ENTER.")

input ("?")

print ("Opening the file...")
file = open (fileName, 'r+') # r+可添加内容  w+是清空后写入新内容
'''
print ("Firstly, Let's check the file's context")
print (file.read())   # 这句为什么不执行？？？
'''
print ("Truncating the file.  Goodbye!")
file.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input ("line 1: ")
line2 = input ("line 2: ")
line3 = input ("line 3: ")


print ("I'm going to write these to the file.")
'''
file.write ("%r %r %r" % line1 line2 line3)
'''
file.write (line1)  # 写入line1的内容
file.write ("\n")   # 打印换行符
file.write (line2)
file.write ("\n")
file.write (line3)
file.write ("\n")

print ("And finally, close '''
file.close()

print ("Print the new %r: "% fileName)
file2 = open (fileName, "r")
print (file2.read())
file2.close()
