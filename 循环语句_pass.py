#pass是空语句，是为了保持程序结构的完整性。

for letter in 'Python': 
   if letter == 'h':
       pass #保持完整性加pass，不加不影响输出。 不能使用语句组。
       print('This is pass block')
   print('Current Letter :', letter)

print("Good bye!")
