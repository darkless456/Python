# web.py 多开访问，刷访问量

import webbrowser as web
import time
import os

count = 0
while count < 10:
    count += 1
    web.open_new_tab('http://blog.sina.com.cn/s/blog_48570ec40101gaf1.html') # 打开网页
    time.sleep(1) # 休眠1s
else:
    exit()

# 进一步：如何自动结束已打开的进程
