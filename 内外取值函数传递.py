def changeme (mylist):
    mylist.append ([1,4,5])
    print ("内取值：" , mylist)
    return

mylist = [9,10,11] # 缩进关系在上面更新优先
changeme (mylist)
print ("外取值：" , mylist)
