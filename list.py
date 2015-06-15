# list.py

ten_things = "Apples Oranges Crows Telephone Light Sugar" # 定义一个字符串

print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ') # 创建stuff列表
print(stuff)

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop(-1) # list.pop(参数[序号])提取出该list的元素
    print("The next_one is ", next_one)
    print("Adding: ", next_one)
    stuff.append(next_one) # 末尾添加新元素
    print("There's %d items now." % len(stuff))

print("There we go: ", stuff)
print("Let's do some things with stuff.")

print(stuff[1]) # 打印序号1的元素

print(stuff[-1]) # 打印序号最末的元素

print(stuff.pop()) # 打印提取的元素

print(stuff)
print(' '.join(stuff)) # join()用来连接字符串 split()用来分割字符串

print(stuff[3:6:2])
print('#'.join(stuff[3:6:2]))

print("Good Bye!")
