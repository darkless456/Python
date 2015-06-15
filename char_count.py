s# char_count.py

mystring = 'hello'

char_count = dict()
for char in mystring:
    count = char_count.get(char, 0)  # radiansdict.get(key, ?),
    '''返回指定键的值，如果值不在字典中返回default值None'''
    count += 1
    char_count[char] = count
print("*" * 50)
print(char_count)
