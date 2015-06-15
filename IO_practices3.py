# coding:utf8
# IO_practices3.py
# 将from_file.txt里内容拷贝到to_file.txt

from sys import argv
from os.path import exists # 导入exists

script, from_file, to_file = argv
prompt = ">> "

print ("Copying from %s to %s"% (from_file, to_file))

file = open (from_file)
indata = file.read()

print ("The input file is %d bytes long"% len (indata))

print ("Does the output file exist? %r"% exists(to_file)) # 确认to_file是否存在
print ("Ready,hit ENTER to continue, CTR-C to abort.")
input(prompt)

tofile = open (to_file, 'w') # r+不能创建文件
tofile.write (indata) # 将from_file里面内容写入

print ("Alright,all done.")

tofile.close()
file.close()
