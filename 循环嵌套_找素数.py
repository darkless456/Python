'''
i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)): #i/j大于等于j
      if not(i%j): break #假如i%j的结果不为真（为假），当i/j的余数为0时，退出循环
      j = j + 1
   if (j > i/j) : print(i, " 是素数")
   i = i + 1

print("Good bye!")
'''

i = 2
while(i < 100):
    j =2
    while((i/j)>= j):
        if not(i%j): break
        j += 1
    if (i/j <j): print(i, " 是素数")
    i += 1

print("Good Bye!")
