# fibs.py

fibs = {0:0, 1:1} # 定义字典，排除例外

def fibonacci(N): # 定义函数
    if N not in fibs: # 不在例外的输入
        number  = fibonacci(N-1) + fibonacci(N-2) #　
        fibs[N] = number
    return fibs[N]

N = int(input('Enter a number: '))
print(fibonacci(N))
