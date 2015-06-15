'''
global VarName的表达式会告诉Python，
VarName是一个全局变量，这样Python就不会在局部命名空间里寻找这个变量了
'''

Money = 2000

def AddMoney():
   # 想改正代码就取消以下注释:
   global Money # 要给全局变量在一个函数里赋值，必须使用global语句。
   Money = Money + 1
   print("函数内值是：" , Money)
   return

print(Money)

AddMoney( )
print(Money)
