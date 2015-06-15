# 在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。

mylist = [10,20,30]  # 定义参数，这个参数位置可以不置顶

# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4]) # 函数内对参数进行更改
 # print("函数内取值: ", mylist)
   return


# 调用changeme函数
changeme( mylist )
print("函数外取值: ", mylist)

