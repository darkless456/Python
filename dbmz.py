# coding: utf-8
import urllib
import urllib.request
import re # 正则库
import time
import sys
import os

print('#'*50)
print('This program is mainly collecting watercress <Do not be shy> group picture')
print('#'*50)
print('Collected before the need to enter a proxy server address, so we can prevent the douban shielding.')
print('Recommend a proxy address: http://cn-proxy.com/')
print('Only need to input the server address and port number, do not need to input HTTP')
print('Demo:127.0.0.1:8080')
print('#'*50)

# 代理模块
proxy_input = input('Proxy Server:')
proxy_handler = urllib.request.ProxyHandler({'http':'%s' %proxy_input})
opener = urllib.request.build_opener(proxy_handler)
urllib.request.install_opener(opener)

img_LuJ = input("Images are downloaded path:")
img_LuJ2 = os.path.abspath(img_LuJ) # 返回path规范化的绝对路径，如：'C:\\Windows\\...'
'''os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False。
   os.path.isfile/isdir(path) 如果path（到文件/目录）是一个存在的文件，返回True。否则返回False。
   os.path.splitext() 返回文件路径和扩展名的元组'''
# 获取网页
def gethtml2(url2):
    html2 = urllib.request.urlopen(url2).read().decode('utf-8')
    return  html2

# 获取图片
def gettoimg(html2):
    reg2 = r'http://www.douban.com/group/topic/\d+'
    #添加正则 匹配url路径数字 d+代表获取0-9无限循环 \转义符号
    toplist = re.findall(reg2, html2) # 正则
    x = 0
    #限制下载图片数量
    #输出topicurl 每次输出一个 的循环
    for topicurl in toplist:
        x += 1
    return topicurl

#　下载图片至本地
def download(topic_page):
    reg3 = r'http://img3.douban.com/view/group_topic/large/public/.+\.jpg'
    #获取贴内图片  正则  ".+\" .匹配任意字符 + 匹配前一个字符或无限次 \ 转移符号 也就是匹配所有字符
    imglist = re.findall(reg3, topic_page)
    i = 1
    download_img = None
    for imgurl in imglist:
        #图片id为文件名
        img_numlist = re.findall(r'p\d{7}', imgurl)
        for img_num in img_numlist:
            download_img = urllib.request.urlretrieve(imgurl, img_LuJ2 + '/%s.jpg' %img_num)
            time.sleep(1)
            i += 1
            print(imgurl)
    return download_img

page_end = int(input('Please enter the page number:'))
num_end = page_end*25
num = 0
page_num = 1
while num <= num_end:
    #获取页面数 从 0 开始
    html2 = gethtml2('http://www.douban.com/group/haixiuzu/discussion?start=%d' %num)
    #抽取下载图片
    topicurl = gettoimg(html2)
    topic_page = gethtml2(topicurl)
    download_img = download(topic_page)
    num = page_num*25
    page_num += 1

else:
    print('Program to collect complete')

