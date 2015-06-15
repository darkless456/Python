# list.py
# 定义list的减法

class superlist(list):
#    def __init__(self,b):
#        self.b = b

    def __sub__(self,b):
        a = self[:]
        b = b[:]
        while len(b) > 0:
            b1 = b.pop()
            if b1 in a:
                a.remove(b1)
        return a

print(superlist([1,2,3]) - superlist([3,4]))
