# 打开一个文件
fo = open("foo.txt", "wb") # 打开文件
print("Name of the file: ", fo.name) # 输出打开文件的文件名
print("Closed or not : ", fo.closed) # 输出此文件是否已经关闭，关闭为true
print("Opening mode : ", fo.mode) # 输出打开文件的模式
