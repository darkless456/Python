# fileName:class_init.py

class person:
    def __init__ (self , name):
        self.name = name
    def sayHi (self):
        print ("Hello,my name is", self.name)

# p = person ("Kevin")
# p.sayHi()
person ("Kevin").sayHi()
