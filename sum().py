# sum().py

a = sum([1,3,5])

b = sum(range(1,11,3))

print(a,b)

c = range(1,11,2)
d = range(1,10,1)

# e = sum([i for i in c if i in d]) # 求交集的和
# 等价于
i = []
for j in c:
    if j in d:
        i.append(j)
        
e = sum(i)

print(sum(c))
print(sum(d))

print(e)
