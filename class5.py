# 类定义

class people:

    # 定义基本属性
    name = ''# 空字符串
    age = 0

    # 定义私有属性，私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法（私有方法）,初始化
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s is speaking: I am %d years old" % (self.name, self.age))


p = people('tom',10,30)
p.speak()

# 单继承

class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        # 调用父类的私有方法
        people.__init__(self,n,a,w)
        self.grade = g
    # 覆写父类的方法
    def speak(self):
        print("%s is speaking: I am %d years old,and I am in grade %d" % (self.name,self.age,self.grade))

s = student('ken', 20, 60, 3)
s.speak()

class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("I am %s , I am a speaker! My topic is %s" % (self.name,self.topic))


class sample(speaker,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)

test = sample ('Tim', 25, 80, 4, 'Python')
test.speak()
'''
类方法的覆写——子类覆盖掉父类的方法

def 方法名与父类一致

若是在方法中要使用到父类方法 父类名.方法名

若是将类放到了模块中 

使用时

import A

l = A.类()
'''
