# lstrip() 方法用于截掉字符串左边的空格或指定字符。

str = "     this is string example....wow!!!     "
print(str.lstrip()) # 默认截取左边空格
str = "88888888this is string example....wow!!!8888888"
print(str.lstrip('8')) # 截取左边8的字符
