import urllib.request
import urllib.response
import pickle
import socket

url = 'https://search.douban.com/book/subject_search'

data = {'search_text':'西游记','cat':1001}
data = pickle.dumps(data)
header = {"Host": "search.douban.com",
"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
"Referer":"https://search.douban.com/book/subject_search"
          }

#GET请求
try:
    req = urllib.request.Request(url,data=data,headers=header,method="GET")
    response = urllib.request.urlopen(req)
    if response.getcode() == 200:
        html_text = response.read().decode("utf-8")
    with open("htmlText.html", mode='w', encoding='utf-8') as fp:
        fp.write(html_text)
        ...
except socket.timeout as e:
    print(e)
    ...

#POST请求 Json接口
url = 'http://httpbin.org/post'
header = {"Host": "httpbin.org",
"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.62",
"Referer":"http://httpbin.org/"
          }

data = {"name":"xu"}
data = pickle.dumps(data)
try:
    req = urllib.request.Request(url,data=data,headers=header,method="POST")
    response = urllib.request.urlopen(req)
    if response.getcode() == 200:
        print(response.read().decode())
        ...
    ...
except socket.timeout as e:
    print(e)
    ...

#urllib下载图片
url = 'https://img0.baidu.com/it/u=3643895624,2552772604&fm=253&fmt=auto&app=120&f=JPEG?w=1200&h=675'
response = urllib.request.urlopen(url)
with open('file/baidu.png', 'wb')as fp:
    fp.write(response.read())
    ...





