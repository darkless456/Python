# multiprocessing.py
# -*- coding: utf-8 -*-

import os

print('Process (%s) start...' % os.getpid())
pid = os.CreatProcess ()
if pid == 0:
    print("I'am child process (%s) and my parent is %s." % (os.getpid(), os.getpid()))
else:
    print("I (%s) just creat a child process (%s)." % (os.getpid(), pid))
# 此语句只能在基于UNIX/LINUX系统运行。
