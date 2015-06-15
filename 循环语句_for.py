'''
#for遍历list 或者 stri 循环并输出
for a in 'Python':     # First Example
   print('Current Letter :', a)

fruits = ['banana', 'apple',  'mango']
for b in fruits:        # Second Example
   print('Current fruit :', b)

print("Good bye!")
 '''

#索引遍历list 或者 stri 循环并输出
fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print( 'Current fruit :' , fruits[index])

print( "Good bye!" )
'''
函数 len() 返回列表的长度，即元素的个数。
函数 range() 返回一个序列的数。
'''
