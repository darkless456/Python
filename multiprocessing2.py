# multiprocessing2.py

from multiprocessing import Process
import os

# （单）子进程（线程）要执行的代码

def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
    return

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target = run_proc, args = ('test',))
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动
    print('Process will start.')
    p.start()
    p.join()
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Process End.')
