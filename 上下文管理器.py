# 上下文管理器.py
'''
f = open("new.txt", "w")
print(f.closed)               # whether the file is open
f.write("Hello World!")
f.close()
print(f.closed)
e = open('new.txt','r')
print(e.readline())
'''

# 上下文管理器写法,管理对象的使用范围。缩进结束即终止

with open('new.txt','w') as g: 
    print(g.closed)
    g.write("Bye_bye!")
print(g.closed)
