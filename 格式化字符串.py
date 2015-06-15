# -- coding:utf-8 --

my_name = "Kevin"
my_age = 28
my_weight = 70
my_height = 161
my_eyes = "Black"
my_teeth = "White"
my_hair = "short and black"

print ("Let's talk about %s." % my_name)
print ("He's %d inches tall." % my_height)
print ("He's %d pounds heavy" % my_weight)
print ("Actually that's too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes , my_hair)) # %s与变量一一对应，数目相同
print ("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky,try to get it exactly right

print ("If I add %d ,%d,and %d I get %d." % (my_age, my_height, my_weight\
                                         ,my_age+my_height+my_weight))


'''
Note:
1、格式化字符串注意%s或%d与变量数目应相同。
'''
