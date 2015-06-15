# avg_age1.py

people = [ [ 'John', 42, 'pants' ], [ 'James', 36 ], [ 'Sue', 38 ] ]

total_age = 0

for person in people: # 对于people中的元素[person]
    age = person[1] # 将元素中第2个值传递给age
    total_age = total_age + age
    print (age)

avg_age = total_age / len (people)
print ("Average age:", avg_age)
