# 例1：if 基本用法
# coding = gb2312

flag = False 
name = 'python'      
if name == 'python':         # 判断变量否为'python'
    flag = True		 # 条件成立时设置标志为真
    print('welcome boss')    # 并输出欢迎信息
else:
    print(name)              # 条件不成立时输出变量名称
