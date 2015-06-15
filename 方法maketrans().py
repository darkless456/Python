# maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，
# 第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
# 注：两个字符串的长度必须相同，为一一对应的关系。

# 转换对应字符为新字符

# from string import maketrans   # 必须调用 maketrans 函数。  Python 2.X版本的语句

intab = "Ho" # 区分大小写
outtab = "12"
trantab = str.maketrans(intab, outtab) # str.maketrans()为内建函数 还有bytearray.maketrans()、bytes.maketrans()

str = "Hello Python World"
print(str.translate(trantab))
