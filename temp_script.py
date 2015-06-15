d = {'key':'value'}

if 'key' in d:
    print(d['key'])

else:
    print('not found')
'''等价于'''
print(d.get('key1', 'a\n'))

'''
如果x是d的一个键值，你得到d[x]。如果不是，你得到None（你能检查或者传播它）。
当x不是d的键值的时候，如果None不是你想要的，调用d.get(x, somethingelse) 来替代。
在这种情况下，如果x不是一个键值。你将得到somethingelse的值 
'''
