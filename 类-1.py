class Model (self) :
    var1 = "公有属性var1"
    __var2 = "私有属性var2"
    def func (self) :
        var3 = "函数局部变量"
        __var4 = "对象的私有属性"
        print (var3)

exam = Model ()
exam.Model
print(var1)
