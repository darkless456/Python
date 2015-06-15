# 列表可以修改，而字符串和元组不能

a = [66.25, 333, 333, 1, 1234.5]
print (a.count(333), a.count(66.25), a.count('x')) # 返回 x 在列表中出现的次数。
print ()

print (a.insert(2, -1)) # 在指定位置插入一个元素。如 a.insert(0, x) 会插入到整个列表之前。
print ()

print (a.append(333)) # list末尾加入元素，等价于 a.insert(len(a), x)。
print ()

print (a.index(333)) # 返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
print ()

print (a.remove(333)) # 删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
print ()

print (a.reverse()) # 倒排列表中的元素。
print ()

print (a.sort()) # 对列表中的元素进行排序。
print ()

'''
list.extend(L)    通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。
'''
