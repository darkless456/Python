#使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码.

for letter in 'Python':     # First Example
   if letter == 'h': break
   print('Current Letter :', letter)
  
var = 10                    # Second Example
while var > 0:              
   print('Current variable value :', var)
   var = var -1
   if var == 5: break

print("Good bye!")
