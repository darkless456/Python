# --coding:utf-8 --
# 格式化变量练习

x = "There are %d types of people." % 10 # 定义格式化字符串
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary , do_not) # 变量可以传递字符串

print (x)
print (y)

print ("I said: %r." % x)
print ("I also said: '%s'." % y)

hilarious = True # not False # False # 判断字符串，不用引号.注意首字母大小写
joke_evaluation = "Isn't that joke so funny?! %r" # 判断字符串格式化符号%r

print (joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print (w+e)
