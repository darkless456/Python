# 创建简单类Employee

class Employee:
   'Common base class for all employees'
   empCount = 0 # 类变量，它的值将在这个类的所有实例之间共享。
                         # 可以在内部类或外部类使用Employee.empCount访问。

   def __init__(self, name, salary): # __init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print("Name : ", self.name,  ", Salary: ", self.salary)


# 创建实例对象
# 要创建一个类的实例，你可以使用类的名称，并通过__init__方法接受参数。

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

# 访问属性
# 可以使用点(.)来访问对象的属性。使用如下类的名称访问类变量:

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

'''
添加，删除，修改类的属性

emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
del emp1.age  # 删除 'age' 属性

也可以使用以下函数的方式来访问属性：

hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')    # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
delattr(empl, 'age')    # 删除属性 'age'
'''

