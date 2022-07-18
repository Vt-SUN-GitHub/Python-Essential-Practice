import threading
import urllib.request
import sys
import time
import json

class ThreadDownloader(threading.Thread):
    def __init__(self, url, savePath, filename):
        super().__init__()
        self.url = url
        self.savePath = savePath
        self.filename = filename
        ...

    def run(self):
        urllib.request.urlretrieve(self.url, self.savePath, self.callback)
        ...

    def callback(self, block, blockSize, contnetLength):
        percent = block * blockSize * 100 / contnetLength
        if percent > 100:
            percent = 100
            ...
        sys.stdout.write("下载完成%d%%" %(percent))
        sys.stdout.flush()
        ...
    ...

if __name__ == '__main__':
    pn = 30
    baseURL = "https://image.baidu.com/search/acjson?tn=resultjson_com&logid=8275658495414653251&ipn=rj" \
              "&ct=201326592&is=&fp=result&fr=&word=%E7%BE%8E%E5%A5%B3&cg=girl&queryWord=%E7%BE%8E%E5%A5%B3&cl=2&lm=-1" \
              "&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=" \
              "&face=0&istype=2&qc=&nc=1&expermode=&nojc=&isAsync=&pn={0}&rn=30&gsm={1}&1658129847650=".format(pn,hex(pn)[2:])
    header = {"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK,q=0.5,en-US;q=0.3,en;q=0.2",
              "Connection":"keep-alive",
              "User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 FireFox/60.0",
              "Upgrade-Insecure-Requests":"1"}
    # for i in range(20):
    newURL = baseURL.format(pn, hex(pn)[2:])
    req = urllib.request.Request(newURL,headers=header)
    jsonStrData = urllib.request.urlopen(req).read().decode('utf-8')
    print(jsonStrData)
    dictObj = json.loads(jsonStrData)
    for item in dictObj['data']:
        if item.get('middleURL'):
            url = item["middleURL"]
            td = ThreadDownloader(url, savePath="file/"+str(time.time())+".png", filename="")
            td.start()
            ...
        time.sleep(3)
        # i +=1
    # ...
    # pn += 30
    ...


