# --coding:utf-8--
# input练习


print ("How old are you ?")
age = str(input ("the age is :"))
print ("the %s is your age." % age)
'''
用%r
How old are you ?
the age is :"11"
the '"11"' is your age.
>>> ================================ RESTART ================================
用%s
How old are you ?
the age is :"11"
the "11" is your age.
注意两者的不同
%r 打印出来的是你写在脚本里的内容，而 %s 打印的是你应该看到的内容。
'''
'''

print ("How tall are you ?")
height = int(input("the height:"))
'''
'''
print （"How much do you weight ?")
weight = int(input("the weight:"))


print ("So, you're %d old, %d tall and %d heavy." % (age, height, weight))
'''
