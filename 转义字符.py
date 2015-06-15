# --coding:utf-8--
# 转义字符练习

tabby_cat = "I'm tabbed in." # "\tI'm tabbed in."
persian_cat = "I'm split\non a line." # \n为换行符号
backslash_cat = "\tI'm a cat" # "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
""" # \t 产生7个空字符

print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

'''
%r 打印出来的是你写在脚本里的内容，而 %s 打印的是你应该看到的内容
'''
