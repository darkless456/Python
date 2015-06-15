# avg_age2.py

people = [ [ 'John', 42 ], [ 'James', 36 ], [ 'Sue', 38 ] ]

ages = [] # 建立空list

for person in people: # 元素person
    age = person [1]
    ages.append (age) # 将age的值加入ages列表中

avg_age = sum (ages) / len (people) # 累加ages列表中元素
print ("Average age:", avg_age)
