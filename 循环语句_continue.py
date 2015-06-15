#continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。

for letter in 'Python':     # First Example
   if letter == 'h': continue
   print('Current Letter :', letter)

var = 10                    # Second Example
while var > 0:              
   var = var -1
   if var == 5: continue
   print('Current variable value :', var)

print("Good bye!")
