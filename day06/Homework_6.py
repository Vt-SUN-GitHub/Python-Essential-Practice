import threading
import urllib.request
import json
import time

class ThreadDownload(threading.Thread):
    def __init__(self, url, savePath):
        super().__init__()
        self.url = url
        self.savePath = savePath
        ...

    def run(self):
        urllib.request.urlretrieve(self.url, self.savePath, self.callback)
        print("图片下载地址为: "+self.url) #显示下载文件的相关信息
        ...

    def callback(self, block, blackSize, contentSize):
        print()
        percent = block * blackSize *100 /contentSize
        if percent > 100:
            percent = 100
            ...
        print("下载完成%d%%" %(percent), end=" ") #下载实时显示下载百分比
        ...
    ...

if __name__ == "__main__":
    length = 1 #48为一页图片数量
    baseURL = "http://pic.sogou.com/napi/pc/searchList?mode=1&start={0}" \
              "&xml_len=48&query=%E7%99%BD%E9%B9%BF".format(length) #确定网络资源的下载地址
    header = {"Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK,q=0.5,en-US;q=0.3,en;q=0.2",
              "Connection": "keep-alive",
              "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 FireFox/60.0",
              "Upgrade-Insecure-Requests": "1"}
    req = urllib.request.Request(baseURL, headers=header)
    jsonStrData = urllib.request.urlopen(req).read().decode('utf-8')
    respDict = json.loads(jsonStrData)
    urlDict = respDict['data']
    for item in urlDict['items']:
        if item.get("oriPicUrl"):
            url = item.get("oriPicUrl")
            td = ThreadDownload(url, savePath="file/bailu-"+str(time.time())+".png")
            td.start()
            time.sleep(3) #过快远程主机会强迫关闭现有链接
        ...
    ...
