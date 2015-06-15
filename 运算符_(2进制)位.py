#按位运算符是把数字看作二进制来进行计算的。返回其对应的10进制值

a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100 与运算
print("Line 1 - Value of c is ", c)

c = a | b;        # 61 = 0011 1101 或运算
print("Line 2 - Value of c is ", c)

c = a ^ b;        # 49 = 0011 0001 异或运算（只有在两个比较的位不同时其结果是1，否则结果为0）
print("Line 3 - Value of c is ", c)

c = ~a;           # -61 = 1100 0011 取反运算
print("Line 4 - Value of c is ", c)

c = a << 2;       # 240 = 1111 0000 左移2位
print("Line 5 - Value of c is ", c)

c = a >> 2;       # 15 = 0000 1111 右移2位
print("Line 6 - Value of c is ", c)
