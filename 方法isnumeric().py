# isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
# 定义一个字符串为Unicode，只需要在字符串前添加 'u' 前缀即可

str = u"this2009"
print(str.isnumeric())

str = u"23443434"
print(str.isnumeric())
