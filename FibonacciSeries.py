# Fibonacci Series
# 两个元素的总和确定了下一个数

a , b = 0 , 1
while b < 10:
    print (b) 
    a , b = b , a+b
    
# 关键字end可以被用于防止输出新的一行，或者在输出的末尾添加不同的字符：

a, b = 0 , 1
while b > 0 and b<1000:
     print(b, end=' ,')
     a , b = b , a+b
 
