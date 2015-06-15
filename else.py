# else.py

numbers = [0,1,2,3,4]
for n in numbers:
    if (n > 2):
        print('the value is %d ' % n)
        break
else:
    print('the end!')

i = 0
while(numbers[i] < 3):
    print('the index %d value is %d' % (i,numbers[i]))
    if numbers[i] < 0:
        break
    i = i + 1
else:
    print('the end!')

