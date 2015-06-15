# ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。
# 如果指定的长度小于原字符串的长度则返回原字符串。

str1 = "Hello Python Programs" # 20长度
print(str1.ljust( 15 , "X" )) # 20为字符长度  X为填充字符，必须为one character大小

str2 = "Hello Programs"
print(str2.ljust( 25 , "Y" ))
