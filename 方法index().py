# str.index(str, beg=0 end=len(string))

str1 = "this is string example....wow!!!"
str2 = "exam" # str2为str1的子字符串

# 检测字符串 str1 中是否包含子字符串 str2
print(str1.index(str2)) # 默认全字符串
print(str1.index(str2, 10)) # 检索到第11个字符
print(str1.index(str2, 40)) # 超出 str1 的长度，报错
