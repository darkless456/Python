 # --coding:utf-8--
# 格式化变量_3

formatter = '%r %r %r %r'

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, not False, not True))
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (\
    "I had this thing.",\
    "That you could type up right.",\
    '''But it didn't sing''',\
    "So I said goodnight.")) # ,号分开输出的字符串，切记！

"""
疑问？
输出结果中带了不需要的单引号，怎么解决？
"""
       
