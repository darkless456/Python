'''
and 布尔"与" - 如果x为False，x and y返回False，否则它返回y的计算值。
or  布尔"或" - 如果x是True，它返回True，否则它返回y的计算值。
not 布尔"非" - 如果x为True，返回False。如果x为False，它返回True。
'''

a = 10
b = 20
c = 0

if ( a and b ): #与
   print("Line 1 - a and b are true")
else:
   print("Line 1 - Either a is not true or b is not true")

if ( a or b ): #或
   print("Line 2 - Either a is true or b is true or both are true")
else:
   print("Line 2 - Neither a is true nor b is true")


a = 0
if ( a and b ):
   print("Line 3 - a and b are true")
else:
   print("Line 3 - Either a is not true or b is not true")

if ( a or b ):
   print("Line 4 - Either a is true or b is true or both are true")
else:
   print("Line 4 - Neither a is true nor b is true")

if not( a and b ): #非
   print("Line 5 - a and b are true")
else:
   print("Line 5 - Either a is not true or b is not true")
