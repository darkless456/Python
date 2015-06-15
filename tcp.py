# tcp.py
# coding:utf-8

# 导入socket库
import socket
# 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接
s.connect(('www.baidu.com', 80))

# 发送数据（http）
s.send(b'GET / HTTP/1.1\r\nHost: www.baidu.com \r\nConnection: close\r\n\r\n')

# 接受数据
buffer = []
while True:
    # 最多接受1024字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break

data = b''.join(buffer)
s.close()

# 接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，
# 把HTTP头打印出来，网页内容保存到文件

header, html = data.split('\r\n\r\n', 1)
print(header)

with open('baidu.html', 'wb') as f:
    f.write(html)
    
