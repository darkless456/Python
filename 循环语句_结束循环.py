# continue（用于跳过该次循环） 和 break（用于退出循环） 用法
'''
i = 1
while 1:   
    i += 1
    if i%2 != 0:     # 非双数时跳过输出
        continue
    print(i)         # 输出双数2、4、6、8、10
    if i > 10:
         break
'''
i=1
while i < 10: #语句已经把 i>=10的退出条件写入
    i+=1
    if i%2 > 0: #取余数非0，终止当前循环并继续下次循环go on while语句
       continue
    print(i)


i = 1
while 1:            # 循环条件为1必定成立
    print(i)         # 输出1~10
    i += 1
    if i > 10:     # 当i大于10时跳出循环
        break
